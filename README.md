#  RAG + Agentic AI System for PDF Chat

This project is a complete implementation of a **Retrieval-Augmented Generation (RAG)** system with **agentic AI capabilities** built using Python. The system allows users to upload PDF files and ask natural language questions based on their contents. It uses a modular agent architecture for retrieval, answering, and verification, powered by Google Gemini and FAISS vector search.

---

## Objective

Build a RAG system that can:

* Ingest and parse PDF files
* Chunk and embed document content using Gemini Embeddings
* Store and retrieve using FAISS vector store
* Use an LLM (Google Gemini Pro) to answer queries
* Validate and refine answers using a verifier agent
* Provide a user-friendly interface via Streamlit

---

##  Features

*  PDF upload and text extraction (supports scanned PDFs too)
*  Robust fallback using PyMuPDF if pdfplumber fails
*  Chunking and embedding using LangChain and Gemini Embeddings
*  FAISS-based vector similarity search
*  Modular agent design:

  * `RetrieverAgent`
  * `QAAgent`
  * `VerifierAgent`
*  RAG pipeline wrapped into a single `run_rag_pipeline()` function
*  Streamlit frontend for chat-based querying
*  CLI and test scripts to validate pipeline functionality

---

##  Tech Stack

| Component        | Technology                                                |           |
| ---------------- | --------------------------------------------------------- | --------- |
| Language         | Python 3.10+                                              |           |
| LLM              | Google Gemini via LangChain                               |           |
| Embeddings       | Gemini `embedding-001` via `langchain_google_genai`       |           |
| Vector DB        | FAISS for similarity search                               |           |
| Document Parsing | pdfplumber (text PDFs)|           |
| Agents Framework | Custom classes (RetrieverAgent, QAAgent, VerifierAgent)   |           |
| Frontend         | Streamlit for interactive user interface                  | Streamlit |

---

##  Folder Structure

```
rag-agentic-system/
├── app/
│   ├── agents/           # Agent definitions (retriever_agent.py, qa_agent.py, verifier_agent.py)
│   ├── chains/           # RAG chain logic (e.g., rag_pipeline.py)
│   ├── utils/            # Loaders, extractors, chunkers (e.g., utils.py)
│   └── __init__.py       # Init for app package
├── data/                 # Uploaded or sample PDFs
├── embeddings/           # FAISS vector store and embedding.py
│   └── embedding.py
├── frontend/             # Streamlit interface
│   └── frontend_app.py
├── tests/                # Unit or functional tests
│   └── test.py
├── main.py               # Entry point to launch full pipeline
├── requirements.txt      # All pip dependencies
├── README.md             # Project overview and instructions
├── .env.example
```

---

##  Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/surajkumar2026/rag-agentic-system.git
cd rag-agentic-system
```

### 2. Create a Virtual Environment

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure Environment Variables (Optional)

use`.env` to load API keys, create the file manually and add:

```env
GOOGLE_API_KEY=your_api_key_here
```

###  With Streamlit UI

```bash
streamlit run app/main.py
```

Then:

* Upload your PDF
* Click "Submit & Process"
* Ask a natural language question

---

##  RAG Pipeline Logic

Implemented in `run_rag_pipeline(query)`:

1. Load FAISS vector DB
2. Retrieve top-k similar chunks
3. Use QA agent to generate an answer
4. Use Verifier agent to validate it
5. Return the final result

---

---

##  Agent Roles

| Agent          | Function                              | Technologies Used                                                   |   |                                     |                                                              |                                     |
| -------------- | ------------------------------------- | ------------------------------------------------------------------- | - | ----------------------------------- | ------------------------------------------------------------ | ----------------------------------- |
| RetrieverAgent | Retrieves top chunks using similarity | FAISS, GoogleGenerativeAIEmbeddings (`langchain_google_genai`)      |   |                                     |                                                              |                                     |
| QAAgent        | Uses Gemini to generate draft answer  | ChatGoogleGenerativeAI, PromptTemplate, `load_qa_chain` (LangChain) |   |                                     |                                                              |                                     |
| VerifierAgent  | Validates and rewrites final answer   | ChatGoogleGenerativeAI, PromptTemplate, LLMChain (LangChain)        |   | Validates and rewrites final answer | ChatGoogleGenerativeAI, PromptTemplate, LLMChain (LangChain) | Validates and rewrites final answer |

---

##  Dependencies

Includes:

* langchain
* langchain\_google\_genai
* faiss-cpu
* pdfplumber
* pymupdf
* pytesseract
* streamlit
* python-dotenv

---

##



##
