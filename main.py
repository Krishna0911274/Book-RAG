from app.embeddings import create_embedding
from app.vectorstore import add_chunk, get_chunks


text = "Habits are the compound interest of self-improvement."

embedding = create_embedding(text)

add_chunk(
    chunk_id="chunk_1",
    text=text,
    embedding=embedding,
    page_number=1
)

data = get_chunks()

print("Stored IDs:", data["ids"])
print("Stored documents:", data["documents"])
print("Stored metadata:", data["metadatas"])