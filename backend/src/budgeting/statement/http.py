from __future__ import annotations
import logging

from fastapi import APIRouter

router = APIRouter(
    prefix="/statements"    
)

@router.post("/")
async def upload():
    logging.info("Uploading a statement")