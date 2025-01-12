from __future__ import annotations
from typing import Optional

from budgeting.database import Entity, Repository
from budgeting.domains import transaction
from budgeting.domains.transaction.models import Transaction
from sqlalchemy import UUID, Connection, DateTime, Numeric, String, Text, insert, select
from sqlalchemy.orm import Mapped, mapped_column, Session
import uuid
from datetime import datetime

class TransactionRepository(Repository):
    """
    
    """
    
    def __init__(self, session: Session):
        """
        
        """
        self._session = session
        
    def find_by_hash(self, hash: str) -> TransactionEntity:
        """
        
        """
        stmt = select(TransactionEntity).where(TransactionEntity.transaction_hash == hash)
        tx = self._session.scalar(stmt)
        return tx
    
    def save(self, model: Transaction) -> TransactionEntity:
        
        entity = TransactionEntity(
            transaction_date=model.transaction_date,
            posting_date=model.date_posted,
            amount=model.transaction_amount,
            description=model.description,
            transaction_hash=model.transaction_hash
        )
        
        self._session.add_all([entity])
        self._session.commit()

class TransactionEntity(Entity):
    """
    
    """
    __tablename__ = "transactions"
    
    id: Mapped[UUID] = mapped_column(Text, primary_key=True, default=uuid.uuid4)
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