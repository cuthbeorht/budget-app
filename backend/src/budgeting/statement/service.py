from __future__ import annotations
from typing import BinaryIO

from budgeting.database import Repository

from budgeting.statement.models import StatementParseCommand
import hashlib

from budgeting.statement.repository import StatementRepository


class StatementParserService:
    """
    
    """
    
    def __init__(self, repository: StatementRepository):
        self._repository = repository
        self._hash = hashlib.new("md5", usedforsecurity=False)
    
    def parse(self, command: StatementParseCommand) -> None:
        for line_no, line in enumerate(command.contents.split("\n")):
            
            # Ignore the header and first few lines
            if line_no < 4:
                
                # Get a hash for the line and see if it already exists
                self._hash.update(line.encode())
                transaction_hash = self._hash.hexdigest()
                
                found = self._repository.find_by_hash(transaction_hash)
                if not found:                                
                    transaction_data = line.split(",")
                

