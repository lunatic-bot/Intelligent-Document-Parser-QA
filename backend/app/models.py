from sqlalchemy import Column,Integer,String
from app.database import Base 
class document(Base):
    __tablename__="documents"
    id=Column(Integer,primary_key=True)
    user_id=Column(Integer)
    filename=Column(String)
    path=Column(String)
    Uploaded_at=Column(String)

