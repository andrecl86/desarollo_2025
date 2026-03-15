from flask import Flask, render_template, request, redirect
from conexion.conexion import obtener_conexion

app = Flask(__name__)

# -------------------------
# PAGINA PRINCIPAL COMIDAS
# -------------------------
@app.route('/')
def index():
    conexion = obtener_conexion()
    cursor = conexion.cursor()

    cursor.execute("SELECT * FROM comidas")
    comidas = cursor.fetchall()

    conexion.close()

    return render_template("index.html", comidas=comidas)


# -------------------------
# AGREGAR COMIDA
# -------------------------
@app.route('/agregar', methods=['POST'])
def agregar():
    nombre = request.form['nombre']
    descripcion = request.form['descripcion']
    precio = request.form['precio']

    conexion = obtener_conexion()
    cursor = conexion.cursor()

    sql = "INSERT INTO comidas (nombre, descripcion, precio) VALUES (%s,%s,%s)"
    valores = (nombre, descripcion, precio)

    cursor.execute(sql, valores)
    conexion.commit()

    conexion.close()

    return redirect('/')


# -------------------------
# MOSTRAR USUARIOS
# -------------------------
@app.route('/usuarios')
def usuarios():
    conexion = obtener_conexion()
    cursor = conexion.cursor()

    cursor.execute("SELECT * FROM usuarios")
    usuarios = cursor.fetchall()

    conexion.close()

    return render_template("usuarios.html", usuarios=usuarios)


# -------------------------
# GUARDAR USUARIO
# -------------------------
@app.route('/guardar_usuario', methods=['POST'])
def guardar_usuario():

    nombre = request.form['nombre']
    mail = request.form['mail']
    password = request.form['password']

    conexion = obtener_conexion()
    cursor = conexion.cursor()

    sql = "INSERT INTO usuarios (nombre, mail, password) VALUES (%s,%s,%s)"
    valores = (nombre, mail, password)

    cursor.execute(sql, valores)
    conexion.commit()

    conexion.close()

    return redirect('/usuarios')


if __name__ == '__main__':
    app.run(debug=True)