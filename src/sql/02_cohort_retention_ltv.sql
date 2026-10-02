-- Clear previous run
DELETE FROM marts.cohort_retention;

-- Perform ETL into the Data Mart
INSERT INTO marts.cohort_retention
WITH user_cohort AS (
    -- CTE 1: Identify First-Purchase Date per User (Cohort Assignment)
    SELECT
        user_id,
        DATE_TRUNC('month', MIN(transaction_date)) AS cohort_month
    FROM raw_transactions
    GROUP BY user_id
),
monthly_activity AS (
    -- CTE 2: Calculate Activity Months & Revenue per Customer
    SELECT
        t.user_id,
        DATE_TRUNC('month', t.transaction_date) AS activity_month,
        SUM(t.revenue) AS monthly_revenue
    FROM raw_transactions t
    GROUP BY t.user_id, DATE_TRUNC('month', t.transaction_date)
),
cohort_base AS (
    -- CTE 3: Join cohorts with activity to find base aggregates
    SELECT
        uc.cohort_month,
        ma.activity_month,
        -- Calculate exact month difference
        ((YEAR(ma.activity_month) - YEAR(uc.cohort_month)) * 12) +
        (MONTH(ma.activity_month) - MONTH(uc.cohort_month)) AS month_index,
        COUNT(DISTINCT ma.user_id) AS active_users,
        SUM(ma.monthly_revenue) AS total_revenue
    FROM user_cohort uc
    JOIN monthly_activity ma ON uc.user_id = ma.user_id
    GROUP BY uc.cohort_month, ma.activity_month
),
cohort_sizes AS (
    -- Get base cohort sizes at month_index 0
    SELECT cohort_month, active_users AS cohort_size
    FROM cohort_base
    WHERE month_index = 0
)
-- Final Select: Apply Window Functions
SELECT
    cb.cohort_month,
    cs.cohort_size,
    cb.activity_month,
    cb.month_index,
    cb.active_users,
    ROUND((cb.active_users::DOUBLE / cs.cohort_size) * 100, 2) AS retention_pct,
    cb.total_revenue,
    SUM(cb.total_revenue) OVER (
        PARTITION BY cb.cohort_month
        ORDER BY cb.month_index
        ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW
    ) AS cumulative_revenue,
    ROUND(SUM(cb.total_revenue) OVER (
        PARTITION BY cb.cohort_month
        ORDER BY cb.month_index
        ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW
    ) / cs.cohort_size, 2) AS cumulative_ltv_per_user
FROM cohort_base cb
JOIN cohort_sizes cs ON cb.cohort_month = cs.cohort_month
ORDER BY cb.cohort_month, cb.month_index;
