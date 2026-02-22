from flask import Flask, render_template

app = Flask(__name__)

# Página principal
@app.route('/')
def inicio():
    return render_template('index.html')

# Página acerca de
@app.route('/about')
def about():
    return render_template('about.html')

# Página productos
@app.route('/productos')
def productos():
    lista_productos = [
        {"nombre": "Pizza", "precio": 5.50},
        {"nombre": "Hamburguesa", "precio": 4.00},
        {"nombre": "Bebida", "precio": 1.50},
        {"nombre": "Postre", "precio": 2.25}
    ]
    return render_template('productos.html', productos=lista_productos)

# Página contacto
@app.route('/contacto')
def contacto():
    return render_template('contacto.html')

if __name__ == '__main__':
    app.run(debug=True)