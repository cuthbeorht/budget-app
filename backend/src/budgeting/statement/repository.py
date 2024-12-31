from __future__ import annotations
from typing import Any
from uuid import UUID
from datetime import datetime

from budgeting.database import Repository
from budgeting.transaction import Transaction

class StatementRepository(Repository):
    """
    
    """
    
    def __init__(self, connection: Any):
        self._connection = connection
        
    def find_by_hash(self, hash: str) -> Transaction:
        pass
    
    def save(self, stmt: Statement) -> Statement:
        pass
    
class Statement:
    id: UUID
    """
    
    """
    
    valid_as_of: datetime
    """
    
    """
    
    number_of_transactions: int
    """
    
    """
    

