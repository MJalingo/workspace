from typing import Optional
from fastapi import FastAPI, Path, Request
from pydantic import BaseModel
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates


app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")


@app.get('/')
async def home(request: Request):
    context = {"request": request}
    return templates.HTMLResponse("index.html", context)

@app.get("/articles/{id}")
def get_articles(id):
    return {'articles':{id}}

