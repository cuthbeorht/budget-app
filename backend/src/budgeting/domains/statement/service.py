from __future__ import annotations

from budgeting.domains.statement.models import StatementParseCommand
import hashlib

from budgeting.domains.transaction.repository import TransactionRepository


class StatementParserService:
    """
    
    """
    
    def __init__(self, transaction_repository: TransactionRepository):
        
        self._transaction_repository = transaction_repository
        self._hash = hashlib.new("md5", usedforsecurity=False)
    
    async def parse(self, command: StatementParseCommand) -> None:
        for line_no, line in enumerate(command.contents):
            
            # Ignore the header and first few lines
            if line_no < 4:
                
                # Get a hash for the line and see if it already exists
                self._hash.update(line.encode())
                transaction_hash = self._hash.hexdigest()
                
                found = self._transaction_repository.find_by_hash(transaction_hash)
                if not found:                                
                    transaction_data = line.split(",")
                

