from fastapi import APIRouter, Depends, File, UploadFile, HTTPException
from sqlalchemy.orm import Session
from typing import List
from sqlalchemy.ext.asyncio import AsyncSession
from app import schemas, models, crud, database
router = APIRouter(prefix="/documents", tags=["documents"])
@router.post("/document",response_model=schemas.Document)
async def create_data(data:schemas.Document,db:AsyncSession=Depends(database.get_db())):
    return await crud.save_details(db,data)


