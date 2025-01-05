from __future__ import annotations
from logging import config

from budgeting.configs import Configuration
from budgeting.database import Repository
from budgeting.domains.statement.repository import StatementRepository
from budgeting.domains.statement.service import StatementParserService
from fastapi import Depends
from sqlalchemy import Engine, create_engine

def configs() -> Configuration:
    return Configuration()

def engine(configuration: Configuration = Depends(configs)) -> Engine:
    create_engine(
        url=f"postgresql://{configuration.database_host}:{configuration.database_port}/{configuration.database_name}",
        echo=True
    )

def statement_repository(engine: Engine = Depends(engine)) -> Repository:
    with engine.connect() as connection:
        return StatementRepository(connection)

def statement_parser_service(repository = Depends(statement_repository)) -> StatementParserService:
    return StatementParserService(repository=repository)
