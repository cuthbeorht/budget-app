from __future__ import annotations

from budgeting.database import Entity, Repository
from budgeting.domains.transaction.models import Transaction
from sqlalchemy import UUID, Connection, DateTime, Numeric, Text
from sqlalchemy.orm import Mapped, mapped_column
import uuid
from datetime import datetime

class TransactionRepository(Repository):
    """
    
    """
    
    def __init__(self, connection: Connection):
        """
        
        """
        self._connection = connection
        
    def find_by_hash(self, hash: str) -> Transaction:
        """
        
        """
        pass

class Transaction(Entity):
    """
    
    """
    __tablename__ = "transactions"
    
    id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    """
    
    """
    
    transaction_date: Mapped[datetime] = mapped_column(DateTime)
    """
    
    """
    
    posting_date: Mapped[datetime] = mapped_column(DateTime)
    """
    
    """
    
    amount: Mapped[float] = mapped_column(Numeric(8, 2))
    """
    
    """
    
    description: Mapped[str] = mapped_column(Text)
    """
    
    """
    
    transaction_hash: Mapped[str] = mapped_column(Text)