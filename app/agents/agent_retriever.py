from langchain_community.vectorstores import FAISS
from langchain_google_genai import GoogleGenerativeAIEmbeddings
import os

class RetrieverAgent:
    def __init__(self):
        self.embeddings= GoogleGenerativeAIEmbeddings(model="models/embedding-001")
        # Load the FAISS index from the local storage
        self.new_db= FAISS.load_local("faiss_index", self.embeddings, allow_dangerous_deserialization=True) 


        # This index is used for similarity search operations.

    def retriever(self, query: str):
        if not query:
            return "Query is empty."
        try:
            docs = self.new_db.similarity_search(query)
            return docs
        except Exception as e:
            return f"Error during retrieval: {e}"
