from app.utils.utils import extract_text_from_pdf, chunk_text
from embeddings.embedding import Embedder
from app.agents.agent_retriever import RetrieverAgent
from app.agents.agent_qa import QAAgent
from app.agents.agent_verifier import VerifierAgent
from app.chains.rag_chain import run_rag_pipeline


text = extract_text_from_pdf("data/Suraj_resume (2).pdf")
embedder = Embedder()
text_chunks, metadatas = chunk_text(text, source="mach_resume.pdf")
vector_store = embedder.get_vector_store(text_chunks, metadatas)
print("Vector store created and saved successfully.")
    
retriever_agent = RetrieverAgent()
    
query = "What is what is candidate's CGPA?"

raw_answer = retriever_agent.retriever(query)
qa_agent = QAAgent()
response = qa_agent.answer_question(query, raw_answer)
verifier_agent = VerifierAgent()
verified_answer = verifier_agent.verify_answer(response, query, raw_answer)

print("\n Query:", query)
print("📄 Top match:", verified_answer)
print("\n Running RAG pipeline...") 



