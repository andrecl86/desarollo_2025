from flask import Flask

app = Flask(__name__)

@app.route("/")
def inicio():
    return "Hola, mi primera pagina en linea 😄"

if __name__ == "__main__":
    app.run(debug=True)
