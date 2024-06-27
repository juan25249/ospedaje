"""query = text("SELECT * FROM libros")
    result = db.execute(query).fetchall()
    return [schemas.Libro(id=row.id, autor=row.autor, titulo=row.titulo, estado=row.estado) for row in result]"""

"""query = text("INSERT INTO libros (autor, titulo, estado) VALUES (:autor, :titulo, :estado)")
db.execute(query, {"autor": libro.autor, "titulo": libro.titulo, "estado": libro.estado})
db.commit()
last_id_query = text("SELECT LAST_INSERT_ID()")
last_id = db.execute(last_id_query).scalar()
return {**libro.dict(), "id": last_id}"""
"""query = text("INSERT INTO usuarios (nombre, documento) VALUES (:nombre, :documento)")
    db.execute(query, {"nombre": usuario.nombre, "documento": usuario.documento})
    db.commit()
    last_id_query = text("SELECT LAST_INSERT_ID()")
    last_id = db.execute(last_id_query).scalar()
    return {**usuario.dict(), "id": last_id}"""

"""query = text("""
        INSERT INTO libros_usuarios (usuario_id, libro_id, tiempo_prestamo)
        VALUES (:usuario_id, :libro_id, :tiempo_prestamo)
    """)
    db.execute(query, {
        "usuario_id": libro_usuario.usuario_id,
        "libro_id": libro_usuario.libro_id,
        "tiempo_prestamo": libro_usuario.tiempo_prestamo,
    })
    db.commit()
    last_id_query = text("SELECT LAST_INSERT_ID()")
    last_id = db.execute(last_id_query).scalar()
    return {**libro_usuario.dict(), "id": last_id}"""