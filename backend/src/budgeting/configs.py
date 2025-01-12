from __future__ import annotations
from typing import Optional

from pydantic_settings import BaseSettings

class Configuration(BaseSettings):
    """
    Fetches environment variables and injects them in this object
    """
    
    database_username: str
    """
    
    """
    
    database_password: str
    """
    
    """
    
    database_host: str
    """
    
    """
    
    database_port: Optional[int] = 5432
    """
    
    """
    
    database_name: str
    """
    
    """