from flask import Flask, render_template, request, redirect, url_for, flash
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from werkzeug.security import check_password_hash, generate_password_hash

# Importamos las funciones de tu servicio (Asegúrate de que los nombres coincidan)
from services.usuario_service import obtener_usuario_por_email, insertar_usuario

app = Flask(__name__)
app.secret_key = 'mi_llave_secreta_para_sesiones' # Puedes poner cualquier texto aquí

# --- 1. CONFIGURACIÓN DE FLASK-LOGIN ---
login_manager = LoginManager(app)
login_manager.login_view = 'login' # Nombre de la función de la ruta de login

# Clase Usuario: Flask-Login necesita este objeto para manejar la sesión
class Usuario(UserMixin):
    def __init__(self, id, email, nombre):
        self.id = id
        self.email = email
        self.nombre = nombre

@login_manager.user_loader
def load_user(user_id):
    # Flask-Login usa esto para "recordar" al usuario. 
    # Por ahora creamos un objeto simple con el ID guardado.
    return Usuario(id=user_id, email="", nombre="")

# --- 2. RUTAS DE LA APLICACIÓN ---

@app.route('/')
@login_required # Solo usuarios logueados pueden ver el index
def index():
    return render_template('index.html', usuario=current_user)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        
        user_data = obtener_usuario_por_email(email)
        
        # Validamos: ¿Existe el usuario? ¿La contraseña coincide con el Hash?
        if user_data and check_password_hash(user_data['password'], password):
            # IMPORTANTE: Usamos 'id_usuario' porque así se llama en tu tabla de MySQL
            usuario_obj = Usuario(
                id=user_data['id_usuario'], 
                email=user_data['email'], 
                nombre=user_data['nombre']
            )
            login_user(usuario_obj)
            return redirect(url_for('index'))
        else:
            flash("Correo o contraseña incorrectos")
            
    return render_template('login.html')

@app.route('/registro', methods=['GET', 'POST'])
def registro():
    if request.method == 'POST':
        nombre = request.form.get('nombre')
        email = request.form.get('email')
        password = request.form.get('password')
        
        # Guardamos en la base de datos
        insertar_usuario(nombre, email, password)
        flash("Registro exitoso. Ya puedes iniciar sesión.")
        return redirect(url_for('login'))
        
    return render_template('registro.html')

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True)