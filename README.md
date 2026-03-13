# AI PDF Q&A Tool

A Python application that allows users to ask questions about the contents of a PDF document using an AI model. The project provides two ways to use the tool:

* **Terminal Version** – Run the program in the command line using `main.py`
* **Web Version** – Use a browser interface powered by FastAPI using `app.py`

Both versions use the same core components for PDF text extraction and AI-powered question answering.

---

## Features

* Extract text from PDF files
* Ask questions about document content
* AI-generated answers using an LLM API
* Command-line interface for quick usage
* FastAPI web interface for browser interaction
* Modular project structure

---

## Project Structure

```
ai_pdf_qa_tool
│
├── main.py              # Terminal-based interface
├── app.py               # FastAPI web application
├── ai_engine.py         # Handles AI API requests
├── pdf_reader.py        # Extracts text from PDF
├── text_chunker.py      # Splits large text into chunks
│
├── templates/
│   └── index.html       # Web UI
│
├── data/                # Uploaded PDFs
│
├── .env                 # Environment variables
├── requirements.txt
└── README.md
```

---

## Requirements

Python 3.9 or higher is recommended.

Install dependencies:

```
pip install -r requirements.txt
```

Example `requirements.txt`:

```
fastapi
uvicorn
python-multipart
jinja2
pypdf
openai
python-dotenv
requests
```

---

## Environment Variables

Create a `.env` file in the project root:

```
OPENROUTER_API_KEY=your_api_key_here
```

The application uses this key to access the AI model API.

---

## Running the Terminal Version

The terminal version allows you to interact with the tool directly from the command line.

Run:


```
edit env file with your api key and pdf path

```
python main.py
```

Example workflow:

1. The program loads the PDF.
2. You enter a question in the terminal.
3. The AI returns an answer based on the document content.

Example:

```
Ask a question about the PDF:
> What is the main topic of the document?
```

---

## Running the FastAPI Web Application

The web version provides a simple browser interface.

Start the server:

```
python -m uvicorn app:app --reload
```

Open your browser:

```
http://127.0.0.1:8000
```

Steps:

1. Upload a PDF file.
2. Enter a question in the input field.
3. The server processes the request and returns the AI-generated answer.

---

## Notes

* Large PDFs may need text chunking to stay within token limits.
* The `data/` directory is used to store uploaded files.
* Ensure the `.env` file contains a valid API key.

---

## Future Improvements

Possible extensions include:

* Chat-style interface for document conversations
* Semantic search for better context retrieval
* Support for multiple PDFs
* Deployment to a cloud service

---

## License

This project is for educational and experimentation purposes.
