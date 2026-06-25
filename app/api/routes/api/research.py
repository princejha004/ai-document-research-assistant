from fastapi import APIRouter

from app.api.routes.services.openai_service import generate_research

from app.api.routes.db.database import SessionLocal
from app.api.routes.db.models import Research

router = APIRouter(
    prefix="/research",
    tags=["Research"]
)


@router.get("/")
def research(topic: str):

    report = generate_research(topic)

    db = SessionLocal()

    research_record = Research(
        topic=topic,
        report=report
    )

    db.add(research_record)
    db.commit()

    db.close()

    return {
        "topic": topic,
        "report": report
    }