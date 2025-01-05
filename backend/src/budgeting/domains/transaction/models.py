from __future__ import annotations

from pydantic import BaseModel
from uuid import UUID
from datetime import datetime

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