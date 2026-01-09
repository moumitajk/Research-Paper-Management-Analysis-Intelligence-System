from langchain_community.document_loaders import PyPDFLoader

def load_paper(pdf_path: str):
    loader = PyPDFLoader(pdf_path)
    documents = loader.load()
    return documents
