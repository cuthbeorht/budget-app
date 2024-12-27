from __future__ import annotations

from fastapi import APIRouter

router = APIRouter(
    prefix="/statements"
)

@router.post("/")
async def upload():
    pass