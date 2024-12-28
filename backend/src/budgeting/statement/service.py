from __future__ import annotations
from typing import BinaryIO

from budgeting.database import Repository

from budgeting.statement.models import StatementParseCommand
from ofxparse import OfxParser


class StatementParserService:
    """
    
    """
    
    def __init__(self, repository: Repository):
        self._repository = repository
    
    def parse(self, command: StatementParseCommand) -> None:
        pass        

