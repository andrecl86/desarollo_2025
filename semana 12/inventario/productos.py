import csv
import json
from pathlib import Path

DATA_PATH = Path(__file__).parent / "data"

# ==== TXT ====
def guardar_txt(productos):
    with open(DATA_PATH / "datos.txt", "w") as f:
        for p in productos:
            f.write(f"{p['id']},{p['nombre']},{p['precio']},{p['cantidad']}\n")

def leer_txt():
    productos = []
    with open(DATA_PATH / "datos.txt", "r") as f:
        for linea in f:
            id_, nombre, precio, cantidad = linea.strip().split(",")
            productos.append({
                "id": int(id_),
                "nombre": nombre,
                "precio": float(precio),
                "cantidad": int(cantidad)
            })
    return productos

# ==== JSON ====
def guardar_json(productos):
    with open(DATA_PATH / "datos.json", "w") as f:
        json.dump(productos, f, indent=4)

def leer_json():
    with open(DATA_PATH / "datos.json", "r") as f:
        return json.load(f)

# ==== CSV ====
def guardar_csv(productos):
    with open(DATA_PATH / "datos.csv", "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=["id", "nombre", "precio", "cantidad"])
        writer.writeheader()
        writer.writerows(productos)

def leer_csv():
    productos = []
    with open(DATA_PATH / "datos.csv", "r") as f:
        reader = csv.DictReader(f)
        for row in reader:
            productos.append({
                "id": int(row["id"]),
                "nombre": row["nombre"],
                "precio": float(row["precio"]),
                "cantidad": int(row["cantidad"])
            })
    return productos

# ==== Inicializar archivos con productos base ====
productos_iniciales = [
    {"id": 1, "nombre": "Hamburguesa", "precio": 5.50, "cantidad": 10},
    {"id": 2, "nombre": "Papas Fritas", "precio": 2.50, "cantidad": 20},
    {"id": 3, "nombre": "Refresco", "precio": 1.50, "cantidad": 30},
    {"id": 4, "nombre": "Hot Dog", "precio": 3.00, "cantidad": 15},
    {"id": 5, "nombre": "Pizza porción", "precio": 4.00, "cantidad": 12},
    {"id": 6, "nombre": "Taco", "precio": 2.75, "cantidad": 25},
    {"id": 7, "nombre": "Helado", "precio": 1.75, "cantidad": 20},
    {"id": 8, "nombre": "Batido", "precio": 3.50, "cantidad": 18},
    {"id": 9, "nombre": "Ensalada", "precio": 4.50, "cantidad": 10},
    {"id": 10, "nombre": "Nuggets", "precio": 3.25, "cantidad": 22}
]

# Para inicializar los archivos (solo una vez)
guardar_txt(productos_iniciales)
guardar_json(productos_iniciales)
guardar_csv(productos_iniciales)