from pathlib import Path
from typing import BinaryIO, Generator
from unittest.mock import Mock

from budgeting.statement.models import StatementParseCommand
from budgeting.statement.service import StatementParserService
import pytest

@pytest.fixture
def valid_statement_contents(
    project_root: Path
) -> str:
    valid_statement_path = project_root.joinpath("test/fixtures/statements/valid-credit-card-statement.csv")
    
    with open(valid_statement_path, "r") as f:
        return f.read()


def test_given_valid_statement_csv_parse_expect_transactions_persisted(
    valid_statement_contents: str
):
    service = StatementParserService(
        repository=Mock()
    )
    
    command = StatementParseCommand(contents=valid_statement_contents)
    
    service.parse(command)