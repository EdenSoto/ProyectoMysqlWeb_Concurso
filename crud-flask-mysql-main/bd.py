
import pymysql


def obtener_conexion():
    return pymysql.connect(host='localhost',
                                user='root',
                                password='Soto235',
                                db='concurso')
