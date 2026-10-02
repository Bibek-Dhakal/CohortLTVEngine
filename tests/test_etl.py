import os

import duckdb
import pytest

from src.etl import run_etl


@pytest.fixture
def test_db_setup(tmp_path):
    # Override environment variables for testing
    test_db = tmp_path / "test.duckdb"
    test_marts = tmp_path / "marts"

    os.environ["DB_PATH"] = str(test_db)
    os.environ["MARTS_OUTPUT_DIR"] = str(test_marts)

    # Create mock data
    con = duckdb.connect(str(test_db))
    con.execute("""
        CREATE TABLE raw_transactions AS
        SELECT 1 AS user_id, '2023-01-15'::DATE AS transaction_date, 100.0 AS revenue UNION ALL
        SELECT 1, '2023-02-20'::DATE, 50.0 UNION ALL
        SELECT 2, '2023-01-25'::DATE, 200.0
    """)
    con.close()

    yield

    # Teardown handled by tmp_path


def test_run_etl_success(test_db_setup):
    # Run the ETL
    run_etl()

    # Check outputs
    db_path = os.environ["DB_PATH"]
    con = duckdb.connect(db_path)

    # Check if target table is populated correctly
    result = con.execute(
        "SELECT * FROM marts.cohort_retention ORDER BY cohort_month, month_index"
    ).fetchall()
    assert len(result) > 0

    # user 1 and user 2 both start in Jan 2023 (cohort size = 2)
    jan_cohort = [row for row in result if str(row[0]) == "2023-01-01"]
    assert jan_cohort[0][1] == 2  # Cohort size

    # Check audit log
    audit = con.execute("SELECT status FROM audit.execution_logs").fetchall()
    assert len(audit) == 1
    assert audit[0][0] == "SUCCESS"

    con.close()
