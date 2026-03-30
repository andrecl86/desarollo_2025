from conexion.conexion import conectar 
from werkzeug.security import generate_password_hash

def obtener_usuario_por_email(email):
    conn = conectar() 
    # Esto es lo que arregla el KeyError: 'id'
    cursor = conn.cursor(dictionary=True) 
    cursor.execute("SELECT * FROM usuarios WHERE email = %s", (email,))
    user = cursor.fetchone()
    cursor.close() # <-- Es buena práctica cerrar también el cursor
    conn.close()
    return user

def insertar_usuario(nombre, email, password_plano):
    conn = conectar() 
    cursor = conn.cursor() # Para inserts no es obligatorio el dictionary=True
    
    # IMPORTANTE: Flask-Login suele usar check_password_hash. 
    # Asegúrate de que el método de cifrado coincida con el que uses en el login.
    password_cifrado = generate_password_hash(password_plano)
    
    sql = "INSERT INTO usuarios (nombre, email, password) VALUES (%s, %s, %s)"
    cursor.execute(sql, (nombre, email, password_cifrado))
    
    conn.commit()
    cursor.close()
    conn.close()