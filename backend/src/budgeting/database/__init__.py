from __future__ import annotations
from typing import List
from sqlalchemy.orm import DeclarativeBase

class Entity(DeclarativeBase):
    pass

class Repository:
    """
    
    """
    def save(self, entity: Entity) -> Entity:
        raise NotImplementedError()
    
    def list(self) -> List[Entity]:
        raise NotImplementedError()
    