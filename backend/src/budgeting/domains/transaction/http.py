from __future__ import annotations
from typing import List

from budgeting import services
from budgeting.domains.transaction.models import Transaction
from budgeting.domains.transaction.service import TransactionService
from fastapi import APIRouter, Depends
from pydantic import BaseModel

router = APIRouter(
    prefix="/transactions"
)

@router.get("/")
async def list(service: TransactionService = Depends(services.transaction_service)):
    """
    
    """
    transactions = service.list()
    
    return ListTransactionsResponse(transactions=transactions)
    
class ListTransactionsResponse(BaseModel):
    transactions: List[Transaction]