import streamlit as st
import os

from src.loader import load_paper
from src.chunker import chunk_text
from src.embeddings import embed_chunks
from src.vector_store import build_faiss_index, search_index
from src.rag import answer_question

from sentence_transformers import SentenceTransformer

st.set_page_config(page_title="Research Paper Assistant")

st.title("📄 Research Paper Assistant")
st.write("Upload a research paper PDF and ask questions about it.")

# ---------- Upload ----------
uploaded_file = st.file_uploader(
    "Upload a research paper (PDF)",
    type=["pdf"]
)

if uploaded_file is not None:
    os.makedirs("data/uploads", exist_ok=True)
    file_path = os.path.join("data", "uploads", uploaded_file.name)

    with open(file_path, "wb") as f:
        f.write(uploaded_file.getbuffer())

    st.success(f"PDF uploaded successfully: {uploaded_file.name}")

    # ---------- Question ----------
    question = st.text_input("Ask a question about the paper")

    if question:
        with st.spinner("Thinking..."):
            # Load and process PDF
            docs = load_paper(file_path)
            full_text = "\n".join([doc.page_content for doc in docs])

            chunks = chunk_text(full_text)
            if len(chunks) == 0:
                st.error("No readable text found in this PDF. Please upload a text-based document.")
                st.stop()

            embeddings = embed_chunks(chunks)

            if embeddings is None or len(embeddings) == 0:
                st.error("Could not generate embeddings from this document.")
                st.stop()

            index = build_faiss_index(embeddings)

            # Embed the question
            model = SentenceTransformer("all-MiniLM-L6-v2")
            query_embedding = model.encode([question])

            indices = search_index(index, query_embedding, top_k=5)

            context = "\n\n".join([chunks[i] for i in indices])

            answer = answer_question(context, question)

        st.subheader("Answer")
        st.write(answer)
