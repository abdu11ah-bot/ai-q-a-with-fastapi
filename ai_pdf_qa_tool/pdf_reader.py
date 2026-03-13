from pypdf import PdfReader
from dotenv import load_dotenv
import os
import logging

load_dotenv()
def extract_text_from_pdf(pdf_path=os.getenv("PDF_PATH")):
    logging.info(f"Extracting text from PDF: {pdf_path}")
    reader = PdfReader(pdf_path)
    text = ""
    for page in reader.pages:
        text += page.extract_text()
    logging.info(f"Text extraction completed for PDF: {pdf_path}")
    return text
