# This is a subset of the conftest config for cumulus library.
# Its main goal here is to provide you a duckdb database and some
# This conftest bootstraps a pyarrow cache for use in running tests
import pathlib

from cumulus_library import databases

MOCK_DATA_DIR = f"{pathlib.Path(__file__).parent}/duckdb_data"


# Pre-test actions
def pytest_cmdline_main(config):
    # We're going to regen the pyarrow cache from the raw data
    db, _ = databases.create_db_backend(
        {
            "db_type": "duckdb",
            "database": ":memory:",
            "load_ndjson_dir": MOCK_DATA_DIR,
        }
    )

    db.connection.execute(
        f"COPY pyarrow_cache TO '{MOCK_DATA_DIR}/pyarrow_cache.parquet' (FORMAT parquet)"
    )
