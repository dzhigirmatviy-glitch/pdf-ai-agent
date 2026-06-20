# AI PDF Analyzer

Upload a PDF, ask a question, and get an answer — powered by local LLM.

## Features
- Ask questions based on PDF content
- Works offline (uses Ollama locally)
- Simple web interface
- Built with FastAPI + LangChain + pypdf

## Tech Stack
- Python 3.12+
- FastAPI
- LangChain + Ollama
- pypdf
- HTML / CSS / JS

## Quick Start

1. Clone the repo  
   `git clone https://github.com/dzhigirmatviy-glitch/pdf-ai-agent.git`

2. Install dependencies  
   `pip install -r backend/requirements.txt`

3. Run Ollama  
   `ollama serve`

4. Start the backend  
   `uvicorn backend.app:app --reload --port 8000`

5. Open `frontend/index.html` in your browser

## Example
Upload a PDF, ask: *"What is the main topic?"* — get a clear answer in seconds.

## Use Cases
- Legal document review
- Financial report analysis
- Academic research
- Internal knowledge extraction

## License
MIT
