from fastapi import FastAPI 

from api.document import router as documentRouter
from api.qa import qa_router as qaRouter 

app = FastAPI(title="Intelligent Document QA")

# include auth router elsewhere
app.include_router(documentRouter)
app.include_router(qaRouter)