#AIzaSyDxs0jRMN67R0FGYb36I_cF0HOvbdJTn0Y

import io
import textwrap
from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from fastapi.middleware.cors import CORSMiddleware
import google.generativeai as genai
import requests
from PIL import Image

app = FastAPI()
templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="static"), name="static")

origins = ["http://127.0.0.1:8000"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/", response_class=HTMLResponse)
async def root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/favicon.ico")
async def favicon():
    pass

@app.get("/gemini")
async def query(query: str):
    genai.configure(api_key="AIzaSyDxs0jRMN67R0FGYb36I_cF0HOvbdJTn0Y")
    model = genai.GenerativeModel('gemini-pro')
    response = model.generate_content(query)
    text = response.text.replace('•', '  *')
    return text

@app.get("/gemini/img")
async def queryimg(query: str, image_url: str):
    genai.configure(api_key="AIzaSyDxs0jRMN67R0FGYb36I_cF0HOvbdJTn0Y")
    response = requests.get(image_url)
    img = Image.open(io.BytesIO(response.content))
    model = genai.GenerativeModel('gemini-pro-vision')
    response = model.generate_content([query, img], stream=True)
    response.resolve()
    return response.text