from __future__ import annotations
from typing import Optional

from pydantic import BaseModel
from uuid import UUID
from datetime import datetime

class Transaction(BaseModel):
    id: Optional[UUID] = None
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
    
    description: str
    """
    
    """
    
    transaction_hash: str
    """
    
    """