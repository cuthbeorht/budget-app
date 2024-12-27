from __future__ import annotations

from fastapi import FastAPI
import logging

def app() -> FastAPI:
    # Logging config
    logging_config()
    
    app = FastAPI()
    
    # Setup Routers
    routers()
    
    return app

def routers():
    pass

def logging_config() -> None:    
    logger = logging.getLogger("uvicorn.error")
    logger.setLevel(logging.DEBUG)
    
    logger.info("Logger configured")