from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

templates = Jinja2Templates(directory="templates")
app = FastAPI()

app.mount("/templates/css", StaticFiles(directory="./templates/css"), name="/templates/css")
app.mount("/templates/images", StaticFiles(directory="./templates/images"), name="/templates/images")
app.mount("/templates/pics", StaticFiles(directory="./templates/pics"), name="/templates/pics")
app.mount("/templates/owl-carousel",
          StaticFiles(directory="./templates/owl-carousel"),
          name="/templates/owl-carousel"
)
app.mount("/templates/js", StaticFiles(directory="./templates/js"), name="/templates/js")

@app.get("/", response_class=HTMLResponse)
def main(request: Request):
    return templates.TemplateResponse(request=request, name="index.html")