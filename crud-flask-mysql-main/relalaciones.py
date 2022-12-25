class Cursos():
	def __init__(self,conIDx,desx,regx,feInix,feTerx,punEspx):
		self.__concursoID = conIDx
		self.__descripcion = desx
		self.__region = regx
		self.__fechaInicio = feInix
		self.__fechaTermino	= feTerx
		self.__puntajeEsperado = punEspx

		self.ListaDominio = []
		self.ListaParticipante = []

		def getConcursoID(self):
			return self.__concursoID

		def getDescrupcion(self):
			return self.__descripcion
		
		def getRegion(self):
			return self.__region

		def getFechaInicio(self):
			return self.__fechaInicio

		def getFechaTermino(self):
			return self.__fechaTermino

		def getPuntajeEsperado(self):
			return self.__puntajeEsperado

class Participante ():
	def __init__(self,parIDx,rutx,nomx,direcx,ciux):

		self.__participanteID = parIDx
		self.__rut = rutx
		self.__nombre = nomx
		self.__dirccion = direcx
		self.__ciudad = ciux

		self.ListaConcurso = []
		self.ListaExamen = []

	def getParticipanteID(self):
		return self.__participanteID

	def getRut(self):
		return self.__rut

	def getDirccion(self):
		return self.__dirccion

	def getNombre(self):
		return self.__nombre

	def getCiudad(self):
			return self.__ciudad

class Dominio ():
	def __init__(self,domIDx):
		self.dominioID = domIDx

		self.ListaConcurso = []
		self.ListaCompetemcia = []

	def getDominioID(self):
		return self.__dominioID

class Competencia ():
	pass

class Pregunta():
	pass

class Examen():
	pass

class RealizacionPregunta():
	pass

class PreguntaAlternativa():
	pass

class PregunataEscrita():
	pass
class TerminoPareado():
	pass
class PreguntaOrden():
	pass

def insertar_alumno(nombre, nota, edad):
    with connection.cursor() as cursor:
        try:
            cursor.execute("INSERT INTO alumnos(nombre, nota, edad) VALUES (%s, %s, %s)",(nombre, nota, edad))
            connection.commit()
        except Exception as e:
            raise


def obtener_alumnos():
    #alumnosx = []
    with connection.cursor() as cursor:
        try:
            cursor.execute("SELECT * FROM alumnos")
            alumnosx = cursor.fetchall()
            return alumnosx
        except Exception as e:
            raise


		




	








