from pathlib import Path

import pytest


@pytest.fixture()
def valid_statement_file(
    project_root: Path
) -> Path:
    return project_root.joinpath("test/fixtures/statements/valid-credit-card-statement.csv")

@pytest.fixture()
def valid_statement_contents(
    valid_statement_file: Path
) -> str:
     with open(valid_statement_file, "r") as f:
        return f.read()