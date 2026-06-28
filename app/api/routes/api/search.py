from fastapi import APIRouter

from app.api.routes.db.rag.chroma_store import search_document

from app.api.routes.db.database import SessionLocal
from app.api.routes.db.models import ResearchHistory

router = APIRouter(
    prefix="/search",
    tags=["Search"]
)


@router.get("/")
def search(question: str):

    results = search_document(question)

    documents = results["documents"][0]

    if not documents:
        answer = "No relevant information found."
    else:
        answer = documents[0]

    db = SessionLocal()

    history = ResearchHistory(
        question=question,
        answer=answer
    )

    db.add(history)
    db.commit()

    return {
        "question": question,
        "answer": answer
    }