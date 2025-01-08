from __future__ import annotations

from budgeting.domains.statement.models import StatementParseCommand
from budgeting.domains.statement.service import StatementParserService
import logging
from typing import Annotated
from budgeting.services import statement_parser_service


from fastapi import APIRouter, Depends, File, HTTPException, UploadFile, status

router = APIRouter(
    prefix="/statements"    
)

@router.post("/")
async def upload(
    stmt: UploadFile, 
    service: StatementParserService = Depends(statement_parser_service)
):
    logging.info("Uploading a statement")
    
    if stmt.size == 0:
        logging.error(f"File size is zero")
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Error with file upload")
    
    
    await service.parse(StatementParseCommand(contents=stmt.file.read()))
    
