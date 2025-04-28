
from pydantic import BaseModel 
class Document(BaseModel):
    id:int
    user_id:int
    file_name:str
    path:str
    uploaded_at:str
    