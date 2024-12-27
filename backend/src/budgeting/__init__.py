from __future__ import annotations

from fastapi import FastAPI
import logging

from budgeting.statement.http import router as StatementRouter

def app() -> FastAPI:
    # Logging config
    logging_config()
    
    app = FastAPI(ignore_trailing_slash=True)
    
    # Setup Routers
    routers(app)
    
    return app

def routers(app: FastAPI):
    
    routers_to_configure = [
        StatementRouter
    ]
    
    for router in routers_to_configure:
        logging.info(f"Configuring router: {str(router)}")
        app.include_router(router)

def logging_config() -> None:    
    logging.getLogger("uvicorn.error")
    logging.basicConfig(level=logging.DEBUG)
    
    logging.info("Logger configured")