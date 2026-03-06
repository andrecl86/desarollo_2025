from flask import Flask, render_template, request, redirect, url_for
from inventario.bd import db, Producto
from inventario.productos import guardar_txt, leer_txt, guardar_json, leer_json, guardar_csv, leer_csv

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///inventario.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)

# Crear base de datos si no existe
with app.app_context():
    db.create_all()

@app.route("/")
def index():
    return render_template("index.html")

# Mostrar productos desde archivos
@app.route("/datos/<formato>")
def mostrar_datos(formato):
    if formato == "txt":
        productos = leer_txt()
    elif formato == "json":
        productos = leer_json()
    elif formato == "csv":
        productos = leer_csv()
    else:
        productos = []
    return render_template("datos.html", productos=productos, formato=formato)

# Agregar producto
@app.route("/agregar", methods=["GET", "POST"])
def agregar():
    if request.method == "POST":
        id_ = int(request.form["id"])
        nombre = request.form["nombre"]
        precio = float(request.form["precio"])
        cantidad = int(request.form["cantidad"])

        producto = {"id": id_, "nombre": nombre, "precio": precio, "cantidad": cantidad}

        # Guardar en archivos
        productos_txt = leer_txt()
        productos_txt.append(producto)
        guardar_txt(productos_txt)

        productos_json = leer_json()
        productos_json.append(producto)
        guardar_json(productos_json)

        productos_csv = leer_csv()
        productos_csv.append(producto)
        guardar_csv(productos_csv)

        # Guardar en base de datos
        nuevo_producto = Producto(id=id_, nombre=nombre, precio=precio, cantidad=cantidad)
        db.session.add(nuevo_producto)
        db.session.commit()

        return redirect(url_for("index"))
    return render_template("producto_form.html")

if __name__ == "__main__":
    app.run(debug=True)