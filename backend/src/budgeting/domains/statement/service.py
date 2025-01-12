from __future__ import annotations
import uuid

from budgeting.domains.statement.models import StatementParseCommand
import hashlib

from budgeting.domains.transaction.models import Transaction
from budgeting.domains.transaction.repository import TransactionRepository


class StatementParserService:
    """
    
    """
    
    def __init__(self, transaction_repository: TransactionRepository):
        
        self._transaction_repository = transaction_repository
        self._hash = hashlib.new("md5", usedforsecurity=False)
    
    async def parse(self, command: StatementParseCommand) -> None:
        line_no = 0
        for line in command.contents.split("\n"):
            
            # Ignore the header and first few lines
            if line_no > 2:
                
                # Get a hash for the line and see if it already exists
                self._hash.update(line.encode())
                transaction_hash = self._hash.hexdigest()
                
                found = self._transaction_repository.find_by_hash(transaction_hash)
                if not found:                                
                    transaction_data = line.split(",")
                    tx = Transaction(
                        transaction_date=transaction_data[2],
                        transaction_amount=transaction_data[4],
                        credit_card_number=transaction_data[1],
                        date_posted=transaction_data[3],
                        description=transaction_data[5],
                        transaction_hash=transaction_hash
                    )
                    new_tx = self._transaction_repository.save(tx)

            # Manual increment... Sigh
            line_no += 1

