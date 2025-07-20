from sqlalchemy.future import select 
from sqlalchemy.ext.asyncio import AsyncSession 
import app.models.user_model as model, app.schema.user_schema as schema 
async  def save_details(db:AsyncSession,data:schema.User):
    new_data=model.User(id=data.id,email=data.email,password=data.password)
    db.add(new_data)
    await db.commit()
    db.refresh(new_data)
    return new_data 
async def show_details(db:AsyncSession,user_id:int):
    result=await db.execute(select(model.User).filter(model.User.id==user_id))
    data = result.scalars().first()
    if data is None:
        return "data not found"
    return data 
async def update_details(db:AsyncSession,data=schema.User):
    result=await db.execute(select(model.User).filter(model.User.id==data.id))
    result.id=data.id
    result.email=data.email
    result.password=data.password
    db.commit()

async def delete(db:AsyncSession,user_id:int):
    result=await db.execute(select(model.User).filter(model.User.id==user_id))
    if result is None:
        return "no user exist"
    db.delete(result)
    db.commit()
    return "user deleted succesfully"
