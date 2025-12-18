# This test uses the same synthea dataset that the library project uses
# to set up a local DB for running queries against. You can generate your
# own dataset using the synthea tool, or include a set of data that you've
# validated for not having PHI to check and see if your study is building
# correctly
import os
import pathlib
from unittest import mock
from cumulus_library import cli, databases

STUDY_NAME = "template"
PROJECT_ROOT = pathlib.Path(__file__).parents[1]


@mock.patch.dict(
    os.environ,
    clear=True,
)
def test_study_run(tmp_path):
    # First build the core study so we have our expected tables
    cli.main(duckdb_args(["build", "-t", "core"], tmp_path))
    # Then we'll run our study
    cli.main(duckdb_args(["build", "-t", STUDY_NAME, "-s", "./"], tmp_path))
    # Now we'll connect to the DB and validate we see the expected results

    db = databases.DuckDatabaseBackend(f"{tmp_path}/duck.db")
    db.connect()
    tables = db.connection.execute(
        "SELECT table_name FROM information_schema.tables"
    ).fetchall()
    # we'll remove all the core tables since we're not validating that
    tables = [
        t[0]
        for t in tables
        if not t[0].startswith("core__") and not t[0].startswith("pyarrow")
    ]
    assert tables == [
        "template__condition",
        "template__count_condition",
        "template__count_encounter",
        "template__encounter",
        "template__encounter_valueset",
        "template__lib_transactions",
        "template__meta_date",
        "template__meta_version",
        "template__patient_cohort",
    ]
    condition_count = db.connection.execute(
        f"SELECT * FROM {STUDY_NAME}__count_condition ORDER BY ALL"
    ).fetchall()
    print(condition_count)
    assert condition_count[0] == (1, "10509002", "resolved")
    assert condition_count[-1] == (3, None, None)
    encounter_count = db.connection.execute(
        f"SELECT * FROM {STUDY_NAME}__count_encounter ORDER BY ALL"
    ).fetchall()
    print(encounter_count)
    assert encounter_count[0] == (12, "AMB", "2018-01-01", "ambulatory")
    assert encounter_count[-1] == (12, "AMB", None, "ambulatory")


def duckdb_args(args: list, tmp_path, stats=False):
    """Convenience function for adding duckdb args to a CLI mock"""
    target = str(PROJECT_ROOT / "tests/duckdb_data")

    if args[0] == "build":
        return [
            *args,
            "--db-type",
            "duckdb",
            "--load-ndjson-dir",
            target,
            "--database",
            f"{tmp_path}/duck.db",
        ]
    elif args[0] == "export":
        return [
            *args,
            "--db-type",
            "duckdb",
            "--database",
            f"{tmp_path}/duck.db",
            f"{tmp_path}/export",
        ]
    return [*args, "--db-type", "duckdb", "--database", f"{tmp_path}/duck.db"]
