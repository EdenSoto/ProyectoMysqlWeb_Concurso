from bd import obtener_conexion


def insertar_participante(nombre,direccion, ciudad,contraseña):
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        cursor.execute("INSERT INTO participante(nombre,direccion, ciudad,contraseña) VALUES (%s, %s, %s , %s)",
                       (nombre,direccion, ciudad, contraseña))
    conexion.commit()
    conexion.close()

def obtener_participante():
    conexion = obtener_conexion()
    participante = []
    with conexion.cursor() as cursor:
        cursor.execute("SELECT idparticipante, nombre,direccion, ciudad   FROM participante")
        participante = cursor.fetchall()
    conexion.close()
    return participante


def eliminar_participante(idparticipante):
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        cursor.execute("DELETE FROM participante WHERE idparticipante = %s", (idparticipante,))
    conexion.commit()
    conexion.close()


def obtener_participante_por_id(idparticipante):
    conexion = obtener_conexion()
    participante = None
    with conexion.cursor() as cursor:
        cursor.execute(
            "SELECT idparticipante, nombre, direccion, ciudad, idparticipante FROM participante WHERE idparticipante = %s", (idparticipante,))
        participante = cursor.fetchone()
    conexion.close()
    return participante

def actualizar_participante(nombre,direccion,ciudad, idparticipante):
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        cursor.execute("UPDATE participante SET nombre = %s, direccion = %s, ciudad = %s  WHERE idparticipante = %s",
                       (nombre,direccion, ciudad, idparticipante))
    conexion.commit()
    conexion.close()


