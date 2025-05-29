import mimetypes
from typing import Union, Optional
import pdfplumber
import pytesseract
import fitz
from PIL import Image
from langchain.text_splitter import RecursiveCharacterTextSplitter
import os

def get_mime_type(file: Union[bytes, str]) -> str:

    try:
        if isinstance(file, bytes):
            return 'application/octet-stream'
        elif hasattr(file, 'name'):
            mime_type, _ = mimetypes.guess_type(file.name)
            return mime_type or 'application/octet-stream'
        elif isinstance(file, str):
            mime_type, _ = mimetypes.guess_type(file)
            return mime_type or 'application/octet-stream'
        return 'application/octet-stream'
    except Exception as e:
        print(f"Error determining MIME type: {e}")
        return 'application/octet-stream'



def handle_pdf(file) -> str:
    try:
        # Use pdfplumber to extract text from PDF
        with pdfplumber.open(file) as pdf:
            text = ""
            for page in pdf.pages:
                text += page.extract_text() or ""
            return text.strip()
    except Exception as e:
        # If pdfplumber fails, try using PyMuPDF (fitz)
        try:
            if hasattr(file, 'seek'):
                file.seek(0)
            doc = fitz.open(file)
            text = ""
            for page in doc:
                text += page.get_text()
            return text.strip()
        except Exception as e:
            print(f"Error extracting text from PDF with PyMuPDF: {e}")

    except Exception as e:
        print(f"Error handling PDF file: {e}")
        return ""

def extract_text_image(file) -> str:
    try:
        # Use pytesseract to extract text from image
        image = Image.open(file)
        text = pytesseract.image_to_string(image)
        return text.strip()
    except Exception as e:
        print(f"Error extracting text from image: {e}")
        return ""


def extract_text_image(file) -> str:
    try:
        # Use pytesseract to extract text from image
        image = Image.open(file)
        text = pytesseract.image_to_string(image)
        return text.strip()
    except Exception as e:
        print(f"Error extracting text from image: {e}")
        return ""



def chunk_text(text: str , source: Optional[str] = None) -> list:
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=50,
        
    )
    chunks= text_splitter.split_text(text)
    metadatas = [{"source": source} for _ in chunks]
    return chunks, metadatas


# now we have to extract text from pdf files
# and return it as a string

def extract_text_from_pdf(pdf_path: str) -> str:
    mine_type = get_mime_type(pdf_path)
    if mine_type == 'application/pdf':
        return handle_pdf(pdf_path)
    elif mine_type in ["image/png", "image/jpeg"]:
        return extract_text_image(pdf_path)
    else:
        print(f"Unsupported file type: {mine_type}")
        return ""



def save_file_to_data(file, file_name: str) -> str:
   
    data_dir = "data"
    os.makedirs(data_dir, exist_ok=True)
    
    file_path = os.path.join(data_dir, file_name)
    
    with open(file_path, 'wb') as f:
        f.write(file.read())
    
    return file_path



    

      



    



