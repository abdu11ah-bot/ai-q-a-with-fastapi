import os
from openai import OpenAI
from dotenv import load_dotenv
import logging

load_dotenv()

client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=os.getenv("OPENROUTER_API_KEY")
)

def ask_question(question, context):

    # limit context to avoid token overflow
    context = context[:6000]

    prompt = f"""
    Answer the question based on the document.

    Document:
    {context}

    Question:
    {question}
    """

    logging.info(f"Asking question: {question}")

    response = client.chat.completions.create(
        model="gpt-4o-mini",   # fixed model
        messages=[
            {"role": "user", "content": prompt}
        ]
    )

    logging.info("Question answered")

    return response.choices[0].message.content