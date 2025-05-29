from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.chains.question_answering import load_qa_chain
from langchain.prompts import PromptTemplate
from dotenv import load_dotenv
import os
import google.generativeai as genai

# Load environment variables and configure Google Generative AI
load_dotenv() 
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))  


class QAAgent:
    def __init__(self):
        self.model=ChatGoogleGenerativeAI(model="gemini-1.5-flash", temperature=0.3)

        prompt_template="""You are a helpful assistant. Use the provided context to answer the question.
        
Context:
{context}

Question:
{question}

Answer:"""

        self.prompt= PromptTemplate(template=prompt_template, input_variables=["context", "question"])
        self.chain= load_qa_chain(self.model, chain_type="stuff", prompt=self.prompt)

        # Initialize the chain with the model and prompt

    def answer_question(self, question, context):
        response= self.chain.invoke(
            {"input_documents": context, "question": question},
            return_only_outputs=True
        )
        return response



