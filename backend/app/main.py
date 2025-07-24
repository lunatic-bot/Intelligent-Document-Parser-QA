from fastapi import FastAPI 
from app.models.document_models import Base 
from app.database import engine
from backend.app.api.document_routes import router as documentRouter
from backend.app.api.user_routes import router as userRouter

app = FastAPI(title="Intelligent Document QA")
@app.on_event("startup")
async def on_startup():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

# include auth router elsewhere
app.include_router(documentRouter)
app.include_router(userRouter)