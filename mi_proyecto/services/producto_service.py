from conexion.conexion import conectar

def listar_productos():
    conn = conectar()
    if conn:
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM productos")
        res = cursor.fetchall()
        conn.close()
        return res
    return []

def eliminar_producto_db(id_p):
    conn = conectar()
    if conn:
        cursor = conn.cursor()
        cursor.execute("DELETE FROM productos WHERE id_producto = %s", (id_p,))
        conn.commit()
        conn.close()