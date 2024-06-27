from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.orm import Session
from sqlalchemy import text
from typing import List
from database import SessionLocal, engine, test_connection
import models, schemas

from mainn import usuarios, libros_usuarios

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

@app.post("/libros/", response_model=schemas.Libro)
async def create_libro(libro: schemas.LibroCreate, db: Session = Depends(get_db)):
    db_libro = (models.Libro(autor=libro.autor, titulo=libro.titulo, estado=libro.estado))
    db.add(db_libro)
    db.commit()
    db.refresh(db_libro)
    return db_libro


@app.get("/libros/", response_model=List[schemas.Libro])
async def read_libros(db: Session = Depends(get_db)):
    return db.query(models.Libro).all()


@app.post("/usuarios/", response_model=schemas.Usuario)
async def create_usuario(usuario: schemas.UsuarioCreate, db: Session = Depends(get_db)):
    db_usuario = (models.Usuario(autor=usuario.autor, titulo=usuario.titulo, estado=usuario.estado))
    db.add(db_usuario)
    db.commit()
    db.refresh(db_usuario)
    return db_usuario


@app.get("/usuarios/", response_model=List[schemas.Usuario])
async def read_usuarios(db: Session = Depends(get_db)):
    return db.query(models.Usuario).all()


@app.post("/libros_usuarios/")
async def create_libro_usuario(libro_usuario: schemas.LibroUsuarioCreate, db: Session = Depends(get_db)):
    db_libro_usuario = (models.LibroUsuario(usuarios_id=libro_usuario.usuario_id,
                                            libro_id=libro_usuario.libro_id,
                                            tiempo_prestamo=libro_usuario.tiempo_prestamo))
    db.add(db_libro_usuario)
    db.commit()
    db.refresh(db_libro_usuario)
    return db_libro_usuario



@app.get("/libro/{libro_id}", response_model=schemas.Libro)
async def read_libro(libro_id: int, db: Session = Depends(get_db)):
    query = text("SELECT * FROM libros WHERE id = :libro_id")
    libro = db.execute(query, {"libro_id": libro_id}).fetchone()
    if not libro:
        raise HTTPException(status_code=404, detail="Libro not found")
    return schemas.Libro(id=libro.id, autor=libro.autor, titulo=libro.titulo, estado=libro.estado)



@app.get("/libros/search/", response_model=List[schemas.Libro])
async def search_libros(query: str, db: Session = Depends(get_db)):
    db_libro = db.query(models.Libro).filter(models.Libro.titulo.like(f"%{query}%")).first()
    return db_libro



@app.put("/libro/{libro_id}", response_model=schemas.Libro)
async def update_libro(libro_id: int, libro: schemas.LibroCreate, db: Session = Depends(get_db)):
    query = text("""
        UPDATE libros SET autor = :autor, titulo = :titulo, estado = :estado 
        WHERE id = :libro_id
    """)
    db.execute(query, {"autor": libro.autor, "titulo": libro.titulo, "estado": libro.estado, "libro_id": libro_id})
    db.commit()
    return {**libro.dict(), "id": libro_id}


@app.delete("/libro/{libro_id}", response_model=dict)
async def delete_libro(libro_id: int, db: Session = Depends(get_db)):
    db_libro = db.query(models.Libro).filter(models.Libro.id == libro_id).first()
    return db_libro