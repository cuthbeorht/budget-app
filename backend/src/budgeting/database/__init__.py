from __future__ import annotations
from sqlalchemy.orm import DeclarativeBase

class Entity(DeclarativeBase):
    pass

class Repository:
    """
    
    """
    def save(self, entity: Entity) -> Entity:
        raise NotImplementedError()
    