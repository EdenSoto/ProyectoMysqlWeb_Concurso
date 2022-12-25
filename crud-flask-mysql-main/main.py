
from flask import Flask, render_template, request, redirect, flash
import controlador_concurso
import controlador_participante

app = Flask(__name__)

"""
Definición de rutas
"""


@app.route("/agregar_concurso")
def formulario_agregar_concurso():
    return render_template("agregar_concurso.html")


@app.route("/guardar_concurso", methods=["POST"])
def guardar_concurso():
    nombre= request.form["nombre"]
    descripcion= request.form["nombre"]
    ciudad = request.form["ciudad"]
    region = request.form["region"]
    fechaInicio = request.form["fechaInicio"]
    fechaTermino = request.form["fechaTermino"]
    puntajeEsperado = request.form["puntajeEsperado"]
    controlador_concurso.insertar_concurso(nombre,descripcion, ciudad, region,fechaInicio,fechaTermino,puntajeEsperado)
    # De cualquier modo, y si todo fue bien, redireccionar
    return redirect("/concurso")


@app.route("/")
@app.route("/concurso")
def concurso():
    concurso = controlador_concurso.obtener_concurso()
    return render_template("concurso.html", concurso=concurso)


@app.route("/eliminar_concurso", methods=["POST"])
def eliminar_concurso():
    controlador_concurso.eliminar_concurso(request.form["idconcurso"])
    return redirect("/concurso")


@app.route("/formulario_editar_concurso/<int:idconcurso>")
def editar_concurso(idconcurso):
    # Obtener el juego por ID
    concurso = controlador_concurso.obtener_concurso_por_id(idconcurso)
    return render_template("editar_concurso.html", concurso=concurso)


@app.route("/actualizar_concurso", methods=["POST"])
def actualizar_concurso():
    id = request.form["id"]
    nombre= request.form["nombre"]
    descripcion= request.form["descripcion"]
    ciudad = request.form["ciudad"]
    region = request.form["region"]
    fechaInicio = request.form["fechaInicio"]
    fechaTermino = request.form["fechaTermino"]
    puntajeEsperado = request.form["puntajeEsperado"]
    controlador_concurso.actualizar_concurso(nombre,descripcion, ciudad, region,fechaInicio,fechaTermino,puntajeEsperado, id)
    return redirect("/concurso")

##############################
@app.route("/participante")
def participante():
    participante = controlador_participante.obtener_participante()
    return render_template("participante.html", participante=participante)

@app.route("/actualizar_participante", methods=["POST"])
def actualizar_participante():
    id = request.form["id"]
    nombre= request.form["nombre"]
    direccion= request.form["direccion"]
    ciudad = request.form["ciudad"]
    
    controlador_participante.actualizar_participante(nombre,direccion, ciudad, id)
    return redirect("/participante")

@app.route("/agregar_participante")
def formulario_agregar_participante():
    return render_template("agregar_participante.html")

@app.route("/guardar_participante", methods=["POST"])
def guardar_participante():
    nombre= request.form["nombre"]
    direccion= request.form["direccion"]
    ciudad = request.form["ciudad"]
    contraseña = request.form["contraseña"]
    controlador_participante.insertar_participante(nombre,direccion, ciudad,contraseña)
    # De cualquier modo, y si todo fue bien, redireccionar
    return redirect("/participante")


@app.route("/eliminar_participante", methods=["POST"])
def eliminar_participante():
    controlador_participante.eliminar_participante(request.form["idparticipante"])
    return redirect("/participante")



@app.route("/formulario_editar_participante/<int:idparticipante>")
def editar_participante(idparticipante):
    # Obtener el juego por ID
    participante = controlador_participante.obtener_participante_por_id(idparticipante)
    return render_template("editar_participante.html", participante=participante)
#############################################
@app.route("/examen")
def examen():
    return render_template("examen.html")

@app.route("/examen1")
def examen1():
    return render_template("examen1.html")

@app.route("/examen2")
def examen2():
    return render_template("examen2.html")
@app.route("/examen3")
def examen3():
    return render_template("examen3.html")

@app.route("/elegir")
def elegir():
    return render_template("elegir.html")


# Iniciar el servidor
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8000, debug=True)
