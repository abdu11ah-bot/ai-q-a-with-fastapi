from pdf_reader import extract_text_from_pdf
from ai_engine import ask_question
import os
from dotenv import load_dotenv
from logger import setup_logger
import logging

load_dotenv()

def main():
    setup_logger()
    try:
        file_path = os.getenv("PDF_PATH")
        logging.info(f"Extracting text from PDF: {file_path}")
        print(f"Loading PDF from: {file_path}")
    except Exception as e:
        logging.error(f"Error loading PDF path: {e}")
        return
    try:
        document_text = extract_text_from_pdf(file_path)
        logging.info("Text extraction completed")
        print("PDF loaded successfully. You can now ask questions about the document.")
    except Exception as e:
        logging.error(f"Error extracting text from PDF: {e}")
        return
    while True:
        question = input("Enter your question (or 'exit' to quit): ")
        if question.lower() == 'exit':
            break
        try:
            answer = ask_question(question, document_text)
            print(f"Answer: {answer}")
            logging.info(f"Question asked: {question}")
        except Exception as e:
            logging.error(f"Error asking question: {e}")
            
if __name__ == "__main__":
    main()