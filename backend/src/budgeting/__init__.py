from __future__ import annotations

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import logging

from budgeting.domains.statement.http import router as StatementRouter
from budgeting.domains.transaction.http import router as TransactionRouter

def app() -> FastAPI:
    # Logging config
    logging_config()
    
    app = FastAPI(
        ignore_trailing_slash=True,
        docs_url="/docs",
        redoc_url="/redoc",
        openapi_url="/openapi"
    )
    
    # Setup CORS
    configure_cors(app=app)
    
    # Setup Routers
    routers(app)
    
    return app

def routers(app: FastAPI):
    
    routers_to_configure = [
        StatementRouter,
        TransactionRouter
    ]
    
    for router in routers_to_configure:
        logging.info(f"Configuring router: {str(router)}")
        app.include_router(router)

def logging_config() -> None:    
    logging.getLogger("uvicorn.error")
    logging.basicConfig(level=logging.DEBUG)
    
    logging.info("Logger configured")
    
def configure_cors(app: FastAPI):
    origins = [
        "http://localhost.tiangolo.com",
        "https://localhost.tiangolo.com",
        "http://localhost",
        "http://localhost:8080",
    ]

    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )