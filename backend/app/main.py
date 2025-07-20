from fastapi import FastAPI 
from app.models.document_models import Base 
from app.database import engine
from app.api.document import router as documentRouter
from app.api.user import router as userRouter
# from api.qa import qa_router as qaRouter 

app = FastAPI(title="Intelligent Document QA")
@app.on_event("startup")
async def on_startup():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

# include auth router elsewhere
app.include_router(documentRouter)
app.include_router(userRouter)