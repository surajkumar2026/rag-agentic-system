from langchain_community.vectorstores import FAISS

from langchain_google_genai import GoogleGenerativeAIEmbeddings
from dotenv import load_dotenv
import os
import google.generativeai as genai

load_dotenv()  # Load environment variables from .env
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))  # Set the Google API key

class Embedder:
    def __init__(self, model_name: str = "models/embedding-001"):
        self.embedder = GoogleGenerativeAIEmbeddings(model=model_name)

    def get_vector_store(self, texts: list[str], metadatas: list[dict]) -> FAISS:
        vector_store = FAISS.from_texts(texts, embedding=self.embedder,metadatas=metadatas)
        # Save the vector store locally for future use
        vector_store.save_local("faiss_index")
        return vector_store


    