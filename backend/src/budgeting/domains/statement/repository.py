from __future__ import annotations

from typing import Any
from uuid import UUID
from datetime import datetime
from budgeting.database import Entity

from budgeting.database import Repository
from budgeting.domains.transaction import Transaction
from sqlalchemy import Connection
from sqlalchemy.orm import Mapped, mapped_column

class StatementRepository(Repository):
    """
    
    """
    
    def __init__(self, connection: Connection):
        self._connection = connection
    
    def find_by_id(self, id: UUID) -> Statement:
        pass
    
    def save(self, entity: Statement) -> Statement:
        pass
    
class Statement(Entity):
    
    __tablename__ = "statements"
    
    id: Mapped[UUID] = mapped_column(primary_key=True)
    """
    
    """
    
    valid_as_of: Mapped[datetime]
    """
    
    """
    
    number_of_transactions: Mapped[int]
    """
    
    """


