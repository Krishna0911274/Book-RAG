from sentence_transformers import SentenceTransformer

model = SentenceTransformer('all-MiniLM-L6-v2')

# For Book Embeddings
def create_embeddings(texts):
    embeddings = model.encode(
        texts,
        show_progress_bar = True,
    )
    
    return embeddings.tolist()

# For User Question
def create_embedding(text):
    embedding = model.encode(text)
    
    return embedding.tolist()