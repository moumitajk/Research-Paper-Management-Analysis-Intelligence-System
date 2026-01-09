from loader import load_paper
from chunker import chunk_text
from embeddings import embed_chunks
from vector_store import build_faiss_index, search_index
from rag import answer_question

from sentence_transformers import SentenceTransformer

if __name__ == "__main__":
    pdf_path = "data/papers/sample_paper.pdf"

    docs = load_paper(pdf_path)
    full_text = "\n".join([doc.page_content for doc in docs])

    chunks = chunk_text(full_text)
    embeddings = embed_chunks(chunks)

    index = build_faiss_index(embeddings)

    question = "What problem does this paper solve?"

    model = SentenceTransformer("all-MiniLM-L6-v2")
    query_embedding = model.encode([question])

    indices = search_index(index, query_embedding)

    context = "\n\n".join([chunks[i] for i in indices])

    answer = answer_question(context, question)

    print("\nQUESTION:\n", question)
    print("\nANSWER:\n", answer)
