from fastapi import FastAPI, Request, Depends
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from fastapi.middleware.cors import CORSMiddleware
import google.generativeai as genai
import markdown

app = FastAPI()
templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="static"), name="static")

origins = ["http://127.0.0.1:8000"]

app.add_middleware(
    CORSMiddleware, 
    allow_origins=origins, 
    allow_credentials=True, 
    allow_methods=["*"], 
    allow_headers=["*"]
)

def GenerativeModel():
    genai.configure(api_key="AIzaSyDxs0jRMN67R0FGYb36I_cF0HOvbdJTn0Y")
    return genai.GenerativeModel('gemini-pro')

def convert_to_markdown(paragraph):
    return markdown.markdown(paragraph)

def removeComments(text):
    lines = text.split('\n')
    filtered_lines = [line.split("#")[0] if "#" in line else line for line in lines]
    result_text = '\n'.join(filtered_lines)
    result_text = result_text.replace("```","").replace("python","")
    return result_text

@app.get("/", response_class=HTMLResponse)
async def root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/favicon.ico")
async def favicon():
    pass

@app.get("/gemini")
async def query(query: str, model: GenerativeModel = Depends(GenerativeModel)):
    if not query:
        return ''
    response = model.generate_content(query)
    text = response.text.replace('•', '  *').replace("*", "<i>").replace("python", "")
    html_code = convert_to_markdown(removeComments(text))
    python_code = html_code.replace("```", "").replace("<h1>", "<h7>").replace("</h1>", "</h7>")
    return python_code