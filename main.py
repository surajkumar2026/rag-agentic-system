
from app.chains.rag_chain import run_rag_pipeline
from app.utils.utils import extract_text_from_pdf, chunk_text 
from embeddings.embedding import Embedder 

      
def pipeline(file_path: str, query: str):
  
    text_chunks, metadatas = chunk_text(extract_text_from_pdf(file_path), source=file_path)
    
    vector_store = Embedder().get_vector_store(text_chunks, metadatas)
    
   
    response = run_rag_pipeline(query)
    
    return response
    


