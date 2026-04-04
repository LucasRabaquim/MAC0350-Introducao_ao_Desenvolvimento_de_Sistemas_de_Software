from fastapi import FastAPI, HTTPException, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from Models import Aluno
from contextlib import asynccontextmanager
from fastapi.staticfiles import StaticFiles
from sqlmodel import SQLModel, create_engine, Session, select, func

@asynccontextmanager
async def initFunction(app: FastAPI):
    create_db_and_tables()
    yield

app = FastAPI(lifespan=initFunction)

arquivo_sqlite = "HTMX2.db"
url_sqlite = f"sqlite:///{arquivo_sqlite}"

engine = create_engine(url_sqlite)
app.mount("/Static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory=["Templates", "Templates/Partials"])

def create_db_and_tables():
    SQLModel.metadata.create_all(engine)
 
def buscar_all_alunos(skip, limit):
    with Session(engine) as session:
        query_count =  session.exec(select(func.count(Aluno.id))).one()
        skip = min(skip, query_count - limit)
        query = select(Aluno).offset(skip).limit(limit)
        return session.exec(query).all(), query_count

@app.get("/", response_class=HTMLResponse)
def root(request: Request):
    return templates.TemplateResponse(request, "index.html")

@app.get("/busca", response_class=HTMLResponse)
def busca(request: Request):
    return templates.TemplateResponse(request, "index.html")

# @app.get("/lista", response_class=HTMLResponse)
# def lista(request: Request):
#     alunos = buscar_all_alunos()
#     return templates.TemplateResponse(request, "lista.html", {"alunos": alunos})
    
@app.get("/editarAlunos")
def novoAluno(request: Request):
    return templates.TemplateResponse(request, "options.html")

@app.post("/novoAluno", response_class=HTMLResponse)
def criar_aluno(nome: str = Form(...)):
    with Session(engine) as session:
        novo_aluno = Aluno(nome=nome)
        session.add(novo_aluno)
        session.commit()
        session.refresh(novo_aluno)
        return HTMLResponse(content=f"<p>O(a) aluno(a) {novo_aluno.nome} foi registrado(a)!")

@app.delete("/deletaAluno", response_class=HTMLResponse)
def deletar_aluno(id: int):
    with Session(engine) as session:
        query = select(Aluno).where(Aluno.id == id)
        aluno = session.exec(query).first()
        if (not aluno):
            raise HTTPException(404, "Aluno não encontrado")
        session.delete(aluno)
        session.commit()
        return HTMLResponse(content=f"<p>O(a) aluno(a) {aluno.nome} foi deletado(a)!</p>")

@app.put("/atualizaAluno", response_class=HTMLResponse)
def atualizar_aluno(id: int = Form(...), novoNome: str = Form(...)):
    with Session(engine) as session:
        query = select(Aluno).where(Aluno.id == id)
        aluno = session.exec(query).first()
        if (not aluno):
            raise HTTPException(404, "Aluno não encontrado")
        nomeAntigo = aluno.nome
        aluno.nome = novoNome
        session.commit()
        session.refresh(aluno)
        return HTMLResponse(content=f"<p>O(a) aluno(a) {nomeAntigo} foi atualizado(a) para {aluno.nome}!</p>")

def buscar_alunos(busca, page, limit):
    with Session(engine) as session:
        query = select(Aluno).where((Aluno.nome).contains(busca)).order_by(Aluno.nome).offset(limit*page).limit(limit).order_by(Aluno.nome)
        return session.exec(query).all()

limit = 5
@app.get("/lista", response_class=HTMLResponse)
def lista(request: Request, busca: str | None='', page: int = 0):
    alunos = buscar_alunos(busca, page, limit)
    if(len(alunos) < limit):
        last = True
    else:
        last = len(buscar_alunos(busca, page+1, limit)) < limit
    return templates.TemplateResponse(request, "lista.html", {"alunos": alunos, "page":page,"last":last})

@app.delete("/apagar", response_class=HTMLResponse)
def apagar():
    return ""