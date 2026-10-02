# Testing Strategy

This application utilizes `pytest` alongside `pytest-cov` to guarantee the integrity of data transformations and ensure
robust code coverage.

## Execution

To execute the test suite and view code coverage in the terminal:

```bash
pytest
```

*Note: The test suite runs end-to-end integration tests natively and will output a `tests coverage` summary table
detailing statements, misses, and overall percentage covered (e.g., 100% coverage on `test_etl.py` and core
initialization files).*

## Test Tiers

1. **Unit Testing**: Tests individual components (e.g., correct string parsing).
2. **Integration Testing**: End-to-end simulation. The `test_etl.py` script:
    - Mounts an in-memory test DuckDB.
    - Inserts predetermined transaction rows.
    - Executes the SQL pipeline.
    - Asserts that outputs (Cohort Sizes, Retention Percentages) match mathematical expectations exactly.
    - Validates that execution logs successfully record a `SUCCESS` status.
