from fastapi import FastAPI
from pydantic import BaseModel
from typing import List, Any

app = FastAPI()


@app.get("/")
def read_root():
    return {"hello": "world"}


libros = []
usuarios = []
libros_usuarios = []


class Usuario(BaseModel):
    nobrem: str
    id: int

    def __init__(self, /, **data: Any):
        super().__init__(**data)


class Libro(BaseModel):
    titulo: str
    autor: str
    estado: int = 0
    id: int

    def __init__(self, /, **data: Any):
        super().__init__(**data)

    def guardar_libros(self):
        if self.id is None:
            self.id = len(libros) + 1
            libros.append(self)
        else:
            for libro in libros:
                if libros.id == self.id:
                    libros.autor = self.autor
                    libros.titulo = self.titulo
                    libros.estado = self.estado

    @classmethod
    def consultar(cls, libro_id):
        for libro in libros:
            if libro_id == libro_id:
                return libro
            return None


class LibroUsuario():
    usuario_id: int
    libro_id: int
    tiempo_prestamo: int

    def __init__(self):
        super().__init__(self)


@app.post("/libros")
async def crear_libro(libro: Libro):
    libro.guardar()
    return libro
