from pathlib import Path
from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from config.settings import settings


app = FastAPI()


app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory= settings.BASE_DIR / "templates")


@app.get("/")
def home(request:Request):

	context = {
		"request":request,
		"name":"FastAPI",
	}
	return templates.TemplateResponse("home.html", context)


@app.get("/post/{post_id}/detail")
def post_detail(request:Request, post_id:str):

	context = {
		"request":request,
		"id":post_id,
	}
	return templates.TemplateResponse("detail.html", context)