
from bd import obtener_conexion


def insertar_concurso(nombre,descripcion, ciudad, region,fechaInicio,fechaTermino,puntajeEsperado):
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        cursor.execute("INSERT INTO concurso(nombre,descripcion, ciudad, region,fechaInicio,fechaTermino,puntajeEsperado) VALUES (%s, %s, %s, %s, %s, %s, %s)",
                       (nombre,descripcion, ciudad, region,fechaInicio,fechaTermino,puntajeEsperado))
    conexion.commit()
    conexion.close()


def obtener_concurso():
    conexion = obtener_conexion()
    concurso = []
    with conexion.cursor() as cursor:
        cursor.execute("SELECT idconcurso, nombre,descripcion, ciudad, region,fechaInicio,fechaTermino,puntajeEsperado FROM concurso")
        concurso = cursor.fetchall()
    conexion.close()
    return concurso


def eliminar_concurso(idconcurso):
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        cursor.execute("DELETE FROM concurso WHERE idconcurso = %s", (idconcurso,))
    conexion.commit()
    conexion.close()


def obtener_concurso_por_id(idconcurso):
    conexion = obtener_conexion()
    concurso = None
    with conexion.cursor() as cursor:
        cursor.execute(
            "SELECT idconcurso, nombre, descripcion, ciudad, region,fechaInicio,fechaTermino,puntajeEsperado, idconcurso FROM concurso WHERE idconcurso = %s", (idconcurso,))
        concurso = cursor.fetchone()
    conexion.close()
    return concurso


def actualizar_concurso(nombre,descripcion, ciudad, region,fechaInicio,fechaTermino,puntajeEsperado, idconcurso):
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        cursor.execute("UPDATE concurso SET nombre = %s, descripcion = %s, ciudad = %s,region = %s,fechaInicio = %s,fechaTermino= %s,puntajeEsperado = %s WHERE idconcurso = %s",
                       (nombre,descripcion, ciudad, region,fechaInicio,fechaTermino,puntajeEsperado, idconcurso))
    conexion.commit()
    conexion.close()

###########################################3
