# Research Paper Assistant using Generative AI

## Abstract
The rapid growth of academic literature has made it increasingly difficult for researchers and students to efficiently read and analyze research papers. This project presents a Generative AI–based Research Paper Assistant that enables users to upload academic papers in PDF format and interact with them through natural language queries. The system leverages semantic search and Retrieval-Augmented Generation (RAG) to provide accurate, context-aware answers grounded in the document content.

---

## Objectives
The primary objectives of this project are:
- To automate the analysis of research papers
- To enable semantic question answering over long technical documents
- To reduce hallucinations in LLM responses using document-grounded retrieval
- To provide an interactive interface for academic document exploration

---

## System Overview
The Research Paper Assistant processes uploaded research papers through a structured pipeline consisting of document ingestion, semantic indexing, and context-aware response generation.

---

## Methodology

### 1. Document Ingestion
Research papers are uploaded through a Streamlit-based user interface. Text is extracted from PDF documents using a PDF loader module.

### 2. Text Chunking
Due to the length of academic documents, extracted text is divided into overlapping chunks. This ensures efficient processing and improves retrieval accuracy.

### 3. Embedding Generation
Each text chunk is converted into a dense vector representation using a Sentence Transformer embedding model.

### 4. Semantic Search with FAISS
The embeddings are stored in a FAISS vector index, enabling fast similarity-based retrieval of relevant document sections in response to user queries.

### 5. Retrieval-Augmented Generation (RAG)
For each user query, the most relevant text chunks are retrieved and provided as context to a Large Language Model (LLM). The model generates answers strictly based on the retrieved content, reducing hallucinations.

---

## Architecture
User
→ Streamlit Interface
→ PDF Text Extraction
→ Text Chunking
→ Embedding Generation
→ FAISS Vector Index
→ Relevant Context Retrieval
→ LLM (RAG)
→ Answer Output

---

## Technologies Used
- Python
- Streamlit
- LangChain
- FAISS
- Sentence Transformers
- Groq LLM
- PyPDF

---

## Project Structure
research_ai/
├── app.py
├── requirements.txt
├── README.md
├── data/
│ ├── papers/
│ └── uploads/
├── src/
│ ├── loader.py
│ ├── chunker.py
│ ├── embeddings.py
│ ├── vector_store.py
│ └── rag.py
└── .env

---

## Usage Instructions
1. Clone the repository  
2. Install required dependencies:

pip install -r requirements.txt
3. Create a `.env` file and add the Groq API key:

GROQ_API_KEY=your_groq_api_key
4. Run the application:

streamlit run app.py

---

## Sample Queries
- What is the main objective of this paper?
- What methodology is proposed?
- What are the key contributions of the study?
- What limitations are discussed?
- Provide a summary of the paper.

---

## Limitations
- The system performs best on text-based PDFs
- Scanned PDFs without OCR support may not be processed correctly
- The current implementation supports single-document analysis

---

## Future Work
- Support for multiple research papers
- OCR integration for scanned documents
- Citation extraction and analysis
- Cross-paper comparison
- Research trend analysis over time

---

## Conclusion
This project demonstrates the effective use of Generative AI and semantic search techniques for academic document analysis. By combining vector-based retrieval with LLM-based generation, the system provides accurate and context-aware responses, making it a valuable tool for researchers and students.

---

## Author
Moumita Roy
