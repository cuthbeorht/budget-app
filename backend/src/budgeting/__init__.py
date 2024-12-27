from __future__ import annotations

from fastapi import FastAPI
import logging

from budgeting.statement.http import router as StatementRouter

def app() -> FastAPI:
    # Logging config
    logging_config()
    
    app = FastAPI()
    
    # Setup Routers
    routers(app)
    
    return app

def routers(app: FastAPI):
    
    app.include_router(StatementRouter)

def logging_config() -> None:    
    logger = logging.getLogger("uvicorn.error")
    logger.setLevel(logging.DEBUG)
    
    logger.info("Logger configured")