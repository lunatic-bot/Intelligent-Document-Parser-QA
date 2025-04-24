from fastapi import APIRouter, Depends, File, UploadFile, HTTPException
from sqlalchemy.orm import Session
from typing import List

# QA Router
qa_router = APIRouter(prefix="/qa", tags=["qa"])
