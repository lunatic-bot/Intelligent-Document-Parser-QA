from fastapi import APIRouter, Depends, File, UploadFile, HTTPException
from sqlalchemy.orm import Session
from typing import List
from sqlalchemy.ext.asyncio import AsyncSession
from app.schema.document_schemas import Document
import app.schema.document_schemas as schemas , app.models, app.crud.document_crud as crud , app.database as database


router = APIRouter(prefix="/documents", tags=["documents"])


@router.post("/document",response_model=Document)
async def create_data(data:schemas.Document, db:AsyncSession=Depends(database.get_db)):
    return await crud.save_details(db,data)


