
import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_groq import ChatGroq

load_dotenv()


def main():
    # Google Gemini
    Geminillm = ChatGoogleGenerativeAI(
        model="gemini-2.5-flash",
        temperature=0,
    )
    response = Geminillm.invoke("What is retrieval-augmented generation?")
    print("Google Gemini:", response.content)

    # Groq
    Groqllm = ChatGroq(
        model="llama-3.3-70b-versatile",
        temperature=0,
    )
    response = Groqllm.invoke("What is retrieval-augmented generation?")
    print("Groq:", response.content)


if __name__ == "__main__":
    main()
