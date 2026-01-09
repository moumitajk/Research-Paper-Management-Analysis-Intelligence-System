from sentence_transformers import SentenceTransformer

def embed_chunks(chunks: list[str]):
    model = SentenceTransformer("all-MiniLM-L6-v2")
    embeddings = model.encode(chunks)
    return embeddings
