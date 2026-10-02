# Project Roadmap

This tracker highlights upcoming features and architectural scaling goals.

## Current Milestones

- [x] Initial SQL Transformation Logic (CTEs + Window Functions)
- [x] Python Execution Runner
- [x] 1M+ Row Performance Guarantee validation

## Future Goals

- **Parameterization Layer**: Expose CLI flags in `etl.py` to change cohort grouping from `month` to `week`.
- **Cloud Object Storage**: Add functionality to directly push the output CSV to an S3 bucket or Google Cloud Storage
  bucket.
- **Incremental Loads**: Modify the ETL script to perform incremental inserts rather than `DELETE` and full recomputes.

## Technical Debt

- The data generator script drops random data. More realistic distribution models (e.g., Poisson distribution for
  transaction frequency) would improve Jupyter visualization testing.
