import faiss
import numpy as np

def build_faiss_index(embeddings: np.ndarray):
    if len(embeddings.shape) < 2:
        raise ValueError("Embeddings are empty or invalid.")
    dimension = embeddings.shape[1]
    index = faiss.IndexFlatL2(dimension)
    index.add(embeddings)
    return index

def search_index(index, query_embedding, top_k=5):
    distances, indices = index.search(query_embedding, top_k)
    return indices[0]
