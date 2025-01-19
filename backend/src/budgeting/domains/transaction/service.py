from __future__ import annotations
from typing import List

from budgeting.domains.transaction.models import Transaction
from budgeting.domains.transaction.repository import TransactionRepository
from budgeting.domains.transaction.utils import transaction_from_entity

class TransactionService:
    """
    
    """
    
    def __init__(self, repository: TransactionRepository):
        """
        
        """
        self._repository = repository
        
    def list(self) -> List[Transaction]:
        """
        
        """
        entities = self._repository.list()
        
        return [transaction_from_entity(tx) for tx in entities]