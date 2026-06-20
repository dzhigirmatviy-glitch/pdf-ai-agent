from fastapi import FastAPI, File, UploadFile, Form
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
import os
import tempfile
from pypdf import PdfReader
from langchain_ollama import OllamaLLM

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

llm = OllamaLLM(model="mistral")


def extract_text_from_pdf(file_path):
    reader = PdfReader(file_path)
    text = ""
    for page in reader.pages:
        text += page.extract_text()
    return text


@app.post("/analyze")
async def analyze_document(file: UploadFile = File(...), query: str = Form(...)):
    try:
        with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp:
            content = await file.read()
            tmp.write(content)
            tmp_path = tmp.name

        pdf_text = extract_text_from_pdf(tmp_path)
        os.unlink(tmp_path)

        if not pdf_text.strip():
            return JSONResponse(content={"error": "PDF не содержит текста или он не извлекается."}, status_code=400)

        context = pdf_text[:4000]

        # Прямой вызов LLM без цепочек
        prompt = f"Ответь на вопрос на основе контекста. Если не знаешь — скажи честно.\nКонтекст: {context}\nВопрос: {query}\nОтвет:"
        answer = llm.invoke(prompt)

        return JSONResponse(content={"answer": answer})

    except Exception as e:
        return JSONResponse(content={"error": str(e)}, status_code=500)