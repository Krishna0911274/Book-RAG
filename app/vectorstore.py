import chromadb

client = chromadb.PersistentClient(path="./chroma_db")

collection = client.get_or_create_collection("book_collection")

def add_chunk(chunk_id, text, embedding, page_number):
    collection.add(
        ids = [chunk_id],
        documents = [text],
        embeddings = [embedding],
        metadatas = [{"page_number": page_number}]
    )
    
def get_chunks():
    return collection.get()