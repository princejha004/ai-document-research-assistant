import chromadb
from sentence_transformers import SentenceTransformer

client = chromadb.PersistentClient(path="./chroma_db")

collection = client.get_or_create_collection(
    name="research_documents"
)

model = SentenceTransformer("all-MiniLM-L6-v2")


def chunk_text(text, chunk_size=500):

    chunks = []

    for i in range(0, len(text), chunk_size):
        chunks.append(text[i:i + chunk_size])

    return chunks


def store_document(doc_id: str, text: str):

    chunks = chunk_text(text)

    for index, chunk in enumerate(chunks):

        embedding = model.encode(chunk).tolist()

        collection.add(
            ids=[f"{doc_id}_{index}"],
            documents=[chunk],
            embeddings=[embedding]
        )


def search_document(query: str):

    query_embedding = model.encode(query).tolist()

    results = collection.query(
        query_embeddings=[query_embedding],
        n_results=3
    )

    return results