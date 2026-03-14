from fastapi import FastAPI, HTTPException, UploadFile, File, Form,Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.requests import Request

from pdf_reader import extract_text_from_pdf
from ai_engine import ask_question
from logger import setup_logger

import shutil
import os

app = FastAPI()
templates = Jinja2Templates(directory="templates")

document_text = ""
setup_logger()

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/upload")
async def upload_pdf(file: UploadFile = File(...)):
    global document_text
    try:
        file_location = f"static/data/{file.filename}"
        with open(file_location,'wb') as buffer:
            shutil.copyfileobj(file.file, buffer)
        
        document_text = extract_text_from_pdf(file_location)
        return {"message": "PDF uploaded and text extracted successfully."}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/ask",response_class=HTMLResponse)
async def ask(request: Request,question: str = Form(...)):
    global document_text
    if not document_text:
        raise HTTPException(status_code=400, detail="No document uploaded yet.")
    try:
        answer = ask_question(question, document_text)
    except Exception as e:
        answer = f"Error processing question: {str(e)}"
    try:
        return templates.TemplateResponse(
            "index.html", 
            {
                "request": request,
                "answer": answer,
                "question": question
            }
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))