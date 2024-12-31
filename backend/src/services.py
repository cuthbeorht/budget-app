from __future__ import annotations
from typing import Dict

from budgeting.database import Repository
from budgeting.statement.repository import StatementRepository
from budgeting.statement.service import StatementParserService
from fastapi import Depends



def statement_repository() -> Repository:
    return StatementRepository(object())

def statement_parser_service(repository = Depends(statement_repository)) -> StatementParserService:
    return StatementParserService(repository=repository)