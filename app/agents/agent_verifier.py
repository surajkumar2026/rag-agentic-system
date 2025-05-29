from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.prompts import PromptTemplate
from langchain.chains.llm import LLMChain
from dotenv import load_dotenv
import os
import google.generativeai as genai

load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

class VerifierAgent:
    def __init__(self):
        self.model= ChatGoogleGenerativeAI(model="gemini-1.5-flash", temperature=0.2)

        # Verification prompt template
        self.prompt = PromptTemplate(
            input_variables= ["answer", "context", "question"],
            template="""
You are an answer verifier.

Given the context and a draft answer, your job is to check whether the answer is fully supported by the context.

If the answer is correct and complete, rewrite it clearly and concisely.

If the answer contains information not found in the context, say:
"The answer is not supported by the context."

Context:
{context}

Question:
{question}

Draft Answer:
{answer}

Final Answer:
"""
        )

        self.chain= LLMChain(llm=self.model, prompt=self.prompt)

    def verify_answer(self, answer: str, question: str, context_docs: list):
        # Combine all chunks into one context string
        context="\n\n".join([doc.page_content for doc in context_docs])

        # Run the chain
        final_response= self.chain.run({
            "answer": answer,
            "context": context,
            "question": question
        })

        return final_response.strip()
