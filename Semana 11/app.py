from flask import Flask, render_template, request, redirect, url_for
from database import get_connection, crear_tablas
from models import Producto

app = Flask(__name__)

crear_tablas()

# ============================
# LISTAR PRODUCTOS
# ============================
@app.route('/')
def index():
    conn = get_connection()
    productos_db = conn.execute("SELECT * FROM productos").fetchall()
    conn.close()

    productos = []

    for p in productos_db:
        producto = Producto(p["id"], p["nombre"], p["precio"], p["cantidad"])
        productos.append(producto)

    return render_template("index.html", productos=productos)


# ============================
# AGREGAR PRODUCTO
# ============================
@app.route('/agregar', methods=["GET", "POST"])
def agregar_producto():

    if request.method == "POST":
        nombre = request.form["nombre"]
        precio = float(request.form["precio"])
        cantidad = int(request.form["cantidad"])

        conn = get_connection()
        conn.execute(
            "INSERT INTO productos (nombre, precio, cantidad) VALUES (?, ?, ?)",
            (nombre, precio, cantidad)
        )
        conn.commit()
        conn.close()

        return redirect(url_for("index"))

    return render_template("agregar_producto.html")


# ============================
# EDITAR PRODUCTO
# ============================
@app.route('/editar/<int:id>', methods=["GET", "POST"])
def editar_producto(id):

    conn = get_connection()

    if request.method == "POST":
        nombre = request.form["nombre"]
        precio = float(request.form["precio"])
        cantidad = int(request.form["cantidad"])

        conn.execute(
            "UPDATE productos SET nombre=?, precio=?, cantidad=? WHERE id=?",
            (nombre, precio, cantidad, id)
        )
        conn.commit()
        conn.close()

        return redirect(url_for("index"))

    producto = conn.execute("SELECT * FROM productos WHERE id=?", (id,)).fetchone()
    conn.close()

    return render_template("editar_producto.html", producto=producto)


# ============================
# ELIMINAR PRODUCTO
# ============================
@app.route('/eliminar/<int:id>')
def eliminar_producto(id):

    conn = get_connection()
    conn.execute("DELETE FROM productos WHERE id=?", (id,))
    conn.commit()
    conn.close()

    return redirect(url_for("index"))


# ============================
# BUSCAR PRODUCTO
# ============================
@app.route('/buscar', methods=["GET", "POST"])
def buscar_producto():

    resultado = None

    if request.method == "POST":
        nombre = request.form["nombre"]

        conn = get_connection()
        resultado = conn.execute(
            "SELECT * FROM productos WHERE nombre LIKE ?",
            ('%' + nombre + '%',)
        ).fetchone()
        conn.close()

    return render_template("buscar_producto.html", resultado=resultado)


if __name__ == '__main__':
    app.run(debug=True)