from app.agents.agent_retriever import RetrieverAgent
from app.agents.agent_qa import QAAgent
from app.agents.agent_verifier import VerifierAgent
from langchain_core.output_parsers import StrOutputParser


def run_rag_pipeline(query: str) -> str:
    if not query:
        return " Please enter a valid query."

    # Step 1: Initialize agents
    retriever_agent= RetrieverAgent()
    qa_agent= QAAgent()
    verifier_agent= VerifierAgent()
    output_parser= StrOutputParser()

    #  Retrieve relevant chunks
    try:
        context_docs= retriever_agent.retriever(query)
    except Exception as e:
        return f"Retrieval failed: {e}"

    if not context_docs:
        return " No relevant context found for your query."
#   Generate answer using QA agent
    try:
        qa_response= qa_agent.answer_question(query, context_docs)
        raw_answer = qa_response["output_text"]
    except Exception as e:
        return f" QA generation failed: {e}"

    # Verify and refine the answer
    try:
        final_answer = verifier_agent.verify_answer(raw_answer, query, context_docs)
    except Exception as e:
        return f"Verification failed: {e}"
    
     # Parse output to get only the clean string
    try:
        clean_output = output_parser.parse(final_answer)
    except Exception as e:
        return f"Output parsing failed: {e}"


    return final_answer
