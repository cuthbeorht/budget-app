from __future__ import annotations
from logging import config

from budgeting.configs import Configuration
from budgeting.database import Repository

from budgeting.domains.statement.service import StatementParserService
from budgeting.domains.transaction.repository import TransactionRepository
from fastapi import Depends
from sqlalchemy import Engine, create_engine
from sqlalchemy.orm import Session

def configs() -> Configuration:
    return Configuration()

def engine(configuration: Configuration = Depends(configs)) -> Engine:
    return create_engine(
        url=f"postgresql://{configuration.database_username}:{configuration.database_password}@{configuration.database_host}:{configuration.database_port}/{configuration.database_name}",
        echo=True
    )
    
def session(db_engine: Engine = Depends(engine)) -> Session:
    return Session(db_engine)
    
def transaction_repository(session: Session = Depends(session)) -> TransactionRepository:
    
    return TransactionRepository(session=session)

def statement_parser_service(repository = Depends(transaction_repository)) -> StatementParserService:
    return StatementParserService(transaction_repository=repository)
