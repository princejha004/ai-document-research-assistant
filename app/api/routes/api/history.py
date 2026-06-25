from fastapi import APIRouter
from sqlalchemy.orm import Session

from app.api.routes.db.database import SessionLocal
from app.api.routes.db.models import ResearchHistory

router = APIRouter(
    prefix="/history",
    tags=["History"]
)


@router.get("/")
def get_history():

    db: Session = SessionLocal()

    data = db.query(
        ResearchHistory
    ).order_by(
        ResearchHistory.id.desc()
    ).all()

    return data