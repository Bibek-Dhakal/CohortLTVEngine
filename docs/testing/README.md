# Testing Strategy

This application utilizes `pytest` to guarantee the integrity of data transformations.

## Execution

To execute the test suite and view code coverage:

```bash
pytest
```

## Test Tiers

1. **Unit Testing**: Tests individual components (e.g., correct string parsing).
2. **Integration Testing**: End-to-end simulation. The `test_etl.py` script:
    - Mounts an in-memory test DuckDB.
    - Inserts predetermined transaction rows.
    - Executes the SQL pipeline.
    - Asserts that outputs (Cohort Sizes, Retention Percentages) match mathematical expectations exactly.
