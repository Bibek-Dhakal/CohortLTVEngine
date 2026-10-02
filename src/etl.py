import os
import time

import duckdb
from dotenv import load_dotenv


def run_etl():
    """
    Executes the analytical pipeline.
    1. Connects to database.
    2. Runs schema creation.
    3. Executes heavy Window Function analytics.
    4. Logs execution metadata.
    5. Exports to BI-ready format.
    """
    load_dotenv()
    db_path = os.getenv("DB_PATH", "data/cohort_ltv.duckdb")
    marts_dir = os.getenv("MARTS_OUTPUT_DIR", "data/marts")

    os.makedirs(marts_dir, exist_ok=True)

    start_time = time.time()
    status = "SUCCESS"
    error_msg = None
    rows_processed = 0

    try:
        con = duckdb.connect(db_path)

        # 1. Create Schema
        with open("src/sql/01_create_schema.sql", "r") as f:
            con.execute(f.read())

        # 2. Run Main Transformation
        with open("src/sql/02_cohort_retention_ltv.sql", "r") as f:
            con.execute(f.read())

        # 3. Export Output
        output_csv = os.path.join(marts_dir, "cohort_retention.csv")
        con.execute(f"COPY marts.cohort_retention TO '{output_csv}' (HEADER, DELIMITER ',');")

        # 4. Fetch metrics
        rows_processed = con.execute("SELECT COUNT(*) FROM marts.cohort_retention").fetchone()[0]

    except Exception as e:
        status = "FAILED"
        error_msg = str(e)
        print(f"ETL Failed: {error_msg}")

    finally:
        duration_ms = (time.time() - start_time) * 1000

        # 5. Log Execution
        if "con" in locals():
            try:
                con.execute(
                    """
                    INSERT INTO audit.execution_logs
                    (duration_ms, rows_processed, status, error_message)
                    VALUES (?, ?, ?, ?)
                    """,
                    [duration_ms, rows_processed, status, error_msg],
                )
                print(
                    f"Pipeline finished in {duration_ms:.2f}ms. Status: {status}. Rows output: {rows_processed}."
                )
            except Exception as log_err:
                print(f"Failed to write to audit log: {log_err}")
            finally:
                con.close()


if __name__ == "__main__":
    run_etl()
