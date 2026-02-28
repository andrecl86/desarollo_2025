from database import get_connection
from models import Producto


class Inventario:

    def __init__(self):
        # Diccionario → {id: objeto Producto}
        self.productos = {}
        self.cargar_productos()

    def cargar_productos(self):
        conn = get_connection()
        filas = conn.execute("SELECT * FROM productos").fetchall()
        conn.close()

        self.productos.clear()

        for fila in filas:
            producto = Producto(
                fila["id"],
                fila["nombre"],
                fila["precio"],
                fila["cantidad"]
            )
            self.productos[producto.get_id()] = producto

    # CREATE
    def agregar_producto(self, nombre, precio, cantidad):
        conn = get_connection()
        conn.execute(
            "INSERT INTO productos (nombre, precio, cantidad) VALUES (?, ?, ?)",
            (nombre, precio, cantidad)  # Tupla
        )
        conn.commit()
        conn.close()
        self.cargar_productos()

    # READ
    def obtener_todos(self):
        return list(self.productos.values())  # Lista

    def buscar_por_nombre(self, nombre):
        return [
            p for p in self.productos.values()
            if nombre.lower() in p.get_nombre().lower()
        ]

    # UPDATE
    def actualizar_producto(self, id, precio, cantidad):
        conn = get_connection()
        conn.execute(
            "UPDATE productos SET precio = ?, cantidad = ? WHERE id = ?",
            (precio, cantidad, id)
        )
        conn.commit()
        conn.close()
        self.cargar_productos()

    # DELETE
    def eliminar_producto(self, id):
        conn = get_connection()
        conn.execute("DELETE FROM productos WHERE id = ?", (id,))
        conn.commit()
        conn.close()
        self.cargar_productos()

    # Conjunto → nombres únicos
    def nombres_unicos(self):
        return {p.get_nombre() for p in self.productos.values()}
