from __future__ import annotations

from budgeting.domains.transaction.models import Transaction
from budgeting.domains.transaction.repository import TransactionEntity

def transaction_from_entity(entity: TransactionEntity) -> Transaction:
    """
    
    """
    return Transaction(
            id=entity.id,
            credit_card_number=str(entity.id),
            date_posted=entity.posting_date,
            transaction_date=entity.transaction_date,
            transaction_amount=entity.amount,
            description=entity.description,
            transaction_hash=entity.transaction_hash
        )