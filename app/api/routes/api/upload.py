from fastapi import APIRouter, UploadFile, File
from pypdf import PdfReader
from app.api.routes.rag.chroma_store import store_document
import uuid
import os

router = APIRouter(
    prefix="/upload",
    tags=["Upload"]
)

@router.post("/")
async def upload_pdf(file: UploadFile = File(...)):

    os.makedirs("uploads", exist_ok=True)

    file_path = f"uploads/{file.filename}"

    with open(file_path, "wb") as f:
        f.write(await file.read())

    pdf = PdfReader(file_path)

    text = ""

    for page in pdf.pages:
        text += page.extract_text() or ""

    doc_id = str(uuid.uuid4())

    store_document(
        doc_id=doc_id,
        text=text
    )

    return {
        "document_id": doc_id,
        "filename": file.filename,
        "characters": len(text),
        "preview": text[:500]
    }