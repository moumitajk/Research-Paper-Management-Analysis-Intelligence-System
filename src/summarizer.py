from dotenv import load_dotenv
from langchain_groq import ChatGroq

load_dotenv()

def summarize_paper(text: str) -> str:
    llm = ChatGroq(
        model="llama-3.1-8b-instant",
        temperature=0
    )

    prompt = f"""
    You are an academic research assistant.

    Summarize the following research paper in 5–6 clear bullet points.
    Use a neutral, technical tone.
    Do not hallucinate or add information not present in the paper.

    Paper:
    {text}
    """

    response = llm.invoke(prompt)
    return response.content
