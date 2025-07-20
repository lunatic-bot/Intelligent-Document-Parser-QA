from sqlalchemy.future import select
from sqlalchemy.ext.asyncio import AsyncSession
import app.models.document_models as models, app.schema.document_schemas as schemas
async def save_details(db:AsyncSession, data:schemas.Document):
    new_data=models.document(id=data.id ,user_id=data.user_id,file_name=data.file_name,path=data.file_name,
                             uploaded_at=data.uploaded_at)
    db.add(new_data)
    await db.commit()
    db.refresh(new_data)
    return new_data 
