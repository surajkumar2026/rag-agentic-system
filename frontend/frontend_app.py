import streamlit as st

from app.utils.utils import  save_file_to_data
from main import pipeline

from embeddings.embedding import Embedder
embedder = Embedder()

   

def main():
    st.title("RAG Pipeline with Streamlit")

     

    with st.sidebar:
        st.title("Menu:")
        pdf_docs = st.file_uploader("Upload your PDF Files and Click on the Submit & Process Button", accept_multiple_files=True)
        if pdf_docs:
            for pdf_doc in pdf_docs:
                file_path = save_file_to_data(pdf_doc, pdf_doc.name)
                st.success(f"File {pdf_doc.name} saved successfully at {file_path}")

        if st.button("Submit & Process"):
            with st.spinner("Processing..."):
                 st.write("You can now ask questions based on the uploaded PDF files.")

    user_question = st.text_input("Ask a Question from the PDF Files")
    if user_question:
        response = pipeline(file_path=file_path, query=user_question)
        print("Response:", response)
        st.write("Answer:", response)

           

if __name__ == "__main__":
    main()