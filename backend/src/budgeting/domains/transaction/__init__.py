from __future__ import annotations
from datetime import datetime
from uuid import UUID

from pydantic import BaseModel

class Transaction(BaseModel):
    id: UUID
    """
    
    """
    
    credit_card_number: str
    """
    
    """
    
    transaction_date: datetime
    """
    
    """
    
    date_posted: datetime
    """
    
    """
    
    transaction_amount: float
    """
    
    """