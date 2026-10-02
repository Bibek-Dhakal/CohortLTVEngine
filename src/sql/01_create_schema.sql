-- Create necessary schemas
CREATE SCHEMA IF NOT EXISTS marts;
CREATE SCHEMA IF NOT EXISTS audit;

-- Audit execution log table
CREATE TABLE IF NOT EXISTS audit.execution_logs (
    log_id UUID DEFAULT uuid(),
    execution_time TIMESTAMP DEFAULT current_timestamp,
    duration_ms DOUBLE,
    rows_processed BIGINT,
    status VARCHAR,
    error_message VARCHAR
);

-- Target Data Mart Table
CREATE TABLE IF NOT EXISTS marts.cohort_retention (
    cohort_month DATE,
    cohort_size BIGINT,
    activity_month DATE,
    month_index BIGINT,
    active_users BIGINT,
    retention_pct DOUBLE,
    total_revenue DECIMAL(15,2),
    cumulative_revenue DECIMAL(15,2),
    cumulative_ltv_per_user DECIMAL(15,2)
);
