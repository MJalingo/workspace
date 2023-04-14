from pytube import YouTube
from fastapi import FastAPI, Form, Request
from tkinter.filedialog import askdirectory
import uvicorn
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

description = """
# Youtube video downloader
"""

app = FastAPI(
    title="Captain",
    description=description,
    version="0.0.1",
    terms_of_service="/",
    contact={
        "name": "Nuruddeen",
        "url": "/",
        "email": "email.example.com",
    },
)


app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")

@app.post('/download')
def get_video_link(Link: str = Form(...),filePath: str = Form(...)):
    mp4 = "hello"#YouTube(Link).streams.get_highest_resolution().download()
    return mp4
@app.get("/directory")
def select_path(filePath: str = Form(...)):
    # path = askdirectory()
    # path_label.config(text=path)
    return filePath
@app.get('/', response_class=HTMLResponse)
def home(request: Request):
    context = {"request": request}
    return templates.TemplateResponse("index.html", context)


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)