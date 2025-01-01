from __future__ import annotations

import logging, services
from typing import Annotated


from fastapi import APIRouter, Depends, File, HTTPException, UploadFile, status

router = APIRouter(
    prefix="/statements"    
)

@router.post("/")
async def upload(file: UploadFile):
    logging.info("Uploading a statement")
    
    if file.size == 0:
        logging.error(f"File size is zero")
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Error with file upload")
    
    
    # service.parse(files.file)
    
