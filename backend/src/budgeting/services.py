from __future__ import annotations

from budgeting.database import Repository
from budgeting.statement.repository import StatementRepository
from budgeting.statement.service import StatementParserService
from fastapi import Depends

def statement_repository() -> Repository:
    return StatementRepository("connection")

def statement_parser_service(repository = Depends(statement_repository)) -> StatementParserService:
    return StatementParserService(repository=repository)