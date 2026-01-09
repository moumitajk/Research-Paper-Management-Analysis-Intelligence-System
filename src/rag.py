import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq

# Load environment variables
load_dotenv()

llm = ChatGroq(
    model="llama-3.1-8b-instant",  # safer than 70b
    temperature=0
)

def answer_question(context: str, question: str) -> str:
    prompt = f"""
You are a research assistant.

Answer the question using ONLY the information from the context below.
If the exact wording is not present, infer the answer based on the paper.
Do NOT say "not found" unless the context is completely unrelated.

Context:
{context}

Question:
{question}

Answer in a clear academic tone.
"""

    response = llm.invoke(prompt)
    return response.content
