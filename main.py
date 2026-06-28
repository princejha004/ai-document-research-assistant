from fastapi import FastAPI

from app.api.routes.api.research import router as research_router
from app.api.routes.api.history import router as history_router
from app.api.routes.api.upload import router as upload_router
from app.api.routes.api.search import router as search_router

from app.api.routes.db.database import engine
from app.api.routes.db.models import Base
from app.api.routes.api.auth import router as auth_router

Base.metadata.create_all(bind=engine)

app = FastAPI(title="AI Research Assistant")

app.include_router(research_router)
app.include_router(history_router)
app.include_router(upload_router)
app.include_router(search_router)
app.include_router(auth_router)

@app.get("/")
def root():
    return {
        "status": "AI Research Assistant Running"
    }