# Usage & Configuration

This directory contains instructions on configuring and running the ETL pipeline.

## Environment Variables

Copy `.env.example` to `.env` to configure your settings locally:

| Variable Name      | Description                                   | Default Value            |
|--------------------|-----------------------------------------------|--------------------------|
| `DB_PATH`          | The relative path to the DuckDB file.         | `data/cohort_ltv.duckdb` |
| `MARTS_OUTPUT_DIR` | The destination directory for BI CSV exports. | `data/marts`             |

## Execution Commands

**Generate Testing Data (1M+ Rows):**

```bash
python src/data_generator.py
```

**Run the ETL Pipeline:**

```bash
python src/etl.py
```

The output will automatically populate the DuckDB data warehouse and export a CSV into the `data/marts/` folder suitable
for importing into standard BI tools like Power BI or Tableau.
