# Arquivo main.py

from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory=["Templates", "Templates/Partials"])


curtidas = 0

@app.get("/home",response_class=HTMLResponse)
async def root(request: Request):
    return templates.TemplateResponse(request, "index.html", {"pagina": "/home/pagina1"})

@app.get("/home/pagina1", response_class=HTMLResponse)
async def pag1(request: Request):
    if (not "HX-Request" in request.headers):
        return templates.TemplateResponse(request, "index.html", {"pagina": "/home/pagina1","pageNum":0})
    return templates.TemplateResponse(request, "Pagina1.html", {"checkedtab": "#page1","pageNum":0})

@app.get("/home/pagina2", response_class=HTMLResponse)
async def pag2(request: Request):
    if (not "HX-Request" in request.headers):
        return templates.TemplateResponse(request, "index.html", {"pagina": "/home/pagina2","pageNum":1})
    return templates.TemplateResponse(request, "Pagina2.html", {"checkedtab": "#page2","pageNum":1})

@app.get("/home/jupiter", response_class=HTMLResponse)
async def jupiter(request: Request):
    if (not "HX-Request" in request.headers):
        return templates.TemplateResponse(request, "index.html", {"pagina": "/home/jupiter","pageNum":3})
    return templates.TemplateResponse(request, "jupiter.html", {"checkedtab": "#jupiter","pageNum":3})

@app.post("/curtir",  response_class=HTMLResponse)
async def post_curtir(request: Request):
    global curtidas
    curtidas = curtidas + 1
    return templates.TemplateResponse(request, "curtir.html", {"curtidas": curtidas, "checkedtab": "#likes"})

@app.delete("/curtir",  response_class=HTMLResponse)
async def delete_curtir(request: Request):
    global curtidas
    curtidas = 0
    return templates.TemplateResponse(request, "curtir.html", {"curtidas": curtidas, "checkedtab": "#likes"})

@app.get("/home/curtidas",  response_class=HTMLResponse)
async def get_curtidas(request: Request):
    if (not "HX-Request" in request.headers):
        return templates.TemplateResponse(request, "index.html", {"pagina": "/home/curtidas", "curtidas": curtidas,"pageNum":2})
    return templates.TemplateResponse(request, "curtir.html", {"curtidas": curtidas, "checkedtab": "#likes","pageNum":2})