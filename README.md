# CohortLTV-Engine

**Automated Customer Cohort Retention and Lifetime Value (LTV) Analytics Engine**

Marketing and Product teams lack visibility into user retention and lifetime value across acquisition channels over
time. This project solves that by utilizing an advanced SQL modeling pipeline combined with an automated Python ETL
runner, enabling sub-5-second execution times across millions of rows.

## 🚀 Features

- **Advanced SQL Transformations**: Utilizes Window Functions, CTEs, and aggregated joins in DuckDB/PostgreSQL to
  accurately compute month-over-month retention and rolling LTV.
- **High-Performance Execution**: In-process analytics using DuckDB to process 1,000,000+ transactional rows in under 5
  seconds (benchmarked at ~174ms).
- **Automated ETL**: Built-in pipeline with comprehensive execution metadata logging.
- **BI-Ready Exports**: Outputs dimensional aggregated flat files perfectly formatted for Power BI, Tableau, or Looker.

## 📚 Documentation Index

- [Run Results & Benchmarks](docs/results/README.md)
- [Usage & Configuration](docs/usage/README.md)
- [Architecture & Data Flow](docs/architecture/README.md)
- [Testing Strategy](docs/testing/README.md)
- [Roadmap](docs/roadmap/README.md)
- [Code Quality & Linting](docs/code_quality.md)

## 🛠 Quick Start

1. **Clone the repo**
2. **Set up the environment:**
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # Or .venv\Scripts\activate on Windows
   pip install -e .[dev]
   python src/data_generator.py
   python src/etl.py
   ```
