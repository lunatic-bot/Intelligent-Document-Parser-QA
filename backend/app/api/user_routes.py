from fastapi import APIRouter, Depends, File, UploadFile, HTTPException
from sqlalchemy.orm import Session
from typing import List
from sqlalchemy.ext.asyncio import AsyncSession
from app.schema.user_schema  import User
import  app.crud.user_crud as crud , app.database as database
router = APIRouter(prefix="/user", tags=["user"])
@router.post("/user",response_model=User)
async def create_data(data:User,db:AsyncSession=Depends(database.get_db)):
    return await  crud.save_details(db,data)
@router.get("/user/{user_id}",response_model=User)
async def show_details(user_id:int,db:AsyncSession=Depends(database.get_db)):
    return await crud.show_details(db,user_id)
@router.put("/user/{user_id}")
async def update_details(data:User,db:AsyncSession=Depends(database.get_db)):
    return await crud.update_details(db,data)

@router.delete("/user/{user_id}"
               )
async def delete(user_id:int,db:AsyncSession=Depends(database.get_db)):
    return await crud.delete(db,user_id)
                         


