import sqlite3

DATABASE = "inventario.db"

def get_connection():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn

def crear_tablas():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS productos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL,
            precio REAL NOT NULL,
            cantidad INTEGER NOT NULL
        )
    """)

    # Verificar si la tabla está vacía
    cursor.execute("SELECT COUNT(*) FROM productos")
    cantidad = cursor.fetchone()[0]

    if cantidad == 0:
        productos_iniciales = [
            ("Pizza Hawaiana", 6.50, 10),
            ("Pizza Pepperoni", 6.00, 8),
            ("Hamburguesa Clásica", 4.50, 15),
            ("Hamburguesa Doble Carne", 5.50, 12),
            ("Hot Dog", 3.00, 20),
            ("Papas Fritas", 2.50, 25),
            ("Alitas BBQ", 5.75, 9),
            ("Nuggets de Pollo", 4.25, 14),
            ("Ensalada César", 3.75, 7),
            ("Tacos Mexicanos", 4.80, 11)
        ]

        cursor.executemany(
            "INSERT INTO productos (nombre, precio, cantidad) VALUES (?, ?, ?)",
            productos_iniciales
        )

    conn.commit()
    conn.close()