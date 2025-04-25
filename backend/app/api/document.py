from fastapi import APIRouter, Depends, File, UploadFile, HTTPException
from sqlalchemy.orm import Session
from typing import List

from app import schemes, models, crud, dependencies
#fvgbnh
router = APIRouter(prefix="/documents", tags=["documents"])
