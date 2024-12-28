from budgeting.statement.service import StatementParserService
import pytest



def test_given_valid_statement_csv_parse_expect_transactions_persisted(
    valid_statement_contents: str
):
    service = StatementParserService()
    
    service.parse(statement_file_contents=valid_statement_contents)