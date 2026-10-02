import os

import duckdb
from dotenv import load_dotenv


def generate_mock_data():
    """
    Generates 1,000,000 random e-commerce transactional records.
    Tests the < 5 seconds execution constraint.
    """
    load_dotenv()
    db_path = os.getenv("DB_PATH", "data/cohort_ltv.duckdb")

    os.makedirs(os.path.dirname(db_path), exist_ok=True)

    con = duckdb.connect(db_path)

    print("Generating 1,000,000 mock transaction rows. This takes a moment...")

    # Generate mock transactions spanning 3 years
    con.execute("""
        CREATE TABLE IF NOT EXISTS raw_transactions AS
        SELECT
            -- Random User ID between 1 and 200,000
            (random() * 200000)::INT + 1 AS user_id,

            -- Random transaction date between Jan 2021 and Dec 2023
            '2021-01-01'::DATE + (random() * 1095)::INT AS transaction_date,

            -- Random revenue amount between $10 and $200
            ROUND((random() * 190 + 10)::DECIMAL(10,2), 2) AS revenue
        FROM generate_series(1, 1000000);
    """)

    count = con.execute("SELECT COUNT(*) FROM raw_transactions").fetchone()[0]
    print(f"Success! {count} rows present in `raw_transactions`.")
    con.close()


if __name__ == "__main__":
    generate_mock_data()
