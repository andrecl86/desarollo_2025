import mysql.connector

def conectar(): # <--- Verifica este nombre
    try:
        return mysql.connector.connect(
            host="localhost",
            user="root",
            password="",  
            database="sistema_inventario"
        )
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return None