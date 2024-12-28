from __future__ import annotations

from budgeting.database import Repository

class StatementParserService:
    """
    
    """
    
    def __init__(self, repository: Repository):
        self._repository = repository
    
    def parse(self, statement_file_contents: str) -> None:
        pass