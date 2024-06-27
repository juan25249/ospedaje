from fastapi import FastAPI
from pydantic import BaseModel, constr
from typing import List, Any

app = FastAPI()

@app.get("/")
def read_root():
    return {"hello": "world"}

libros = []
usuarios = []
libros_usuarios = []

class Usuario(BaseModel):
    nombre: str
    id: int

class Libro(BaseModel):
    titulo: constr(min_length=3, max_length=10)
    autor: str
    estado: int = 0
    id: int = None

    def guardar(self):
        if self.id is None:
            self.id = len(libros) + 1
            libros.append(self)
        else:
            for libro in libros:
                if libro.id == self.id:
                    libro.autor = self.autor
                    libro.titulo= self.titulo
                    libro.estado = self.estado
        return self


    @classmethod
    def consultar(cls, libro_id):
        for libro in libros:
            if libro.id == libro_id:
                return libro
        return None

    @classmethod
    def eliminar(cls, libro_id):
        for indic, dato in enumerate(libros):
            if dato.id== libro_id:
                libros.pop(indic)
                return indic
        return None

    def editar(self):
        self.guardar()

    @classmethod
    def consultar_todos(cls):
        return libros


class LibroUsuario():
    usuario_id : int
    libro_id : int
    tiempo_prestamo : int

    def _init_(self):
        pass

@app.post("/libro")
async def crear_libro(libro: Libro):
    return libro.guardar()


@app.get("/libros")
async def consultar_libro():
    return Libro.consultar_todos()

@app.get("/libro/{libro_id}")
async def consultar_libro(libro_id : int):
    return Libro.consultar(libro_id)


@app.delete("/libro/{libro_id}")
async def eliminar_libro(libro_id : int):
    return Libro.eliminar(libro_id)

@app.put("/libro")
async def editar_libro(libro: Libro):
    return libro.editar()









































































