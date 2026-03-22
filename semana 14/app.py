from flask import Flask, render_template, request, redirect, url_for, flash
from flask_mysqldb import MySQL
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.secret_key = 'clave_secreta'

# MYSQL
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''  # cambia si tienes contraseña
app.config['MYSQL_DB'] = 'desarrollo_web'

mysql = MySQL(app)

# LOGIN
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

# CLASE USUARIO
class Usuario(UserMixin):
    def __init__(self, id, nombre, email):
        self.id = id
        self.nombre = nombre
        self.email = email

# CARGAR USUARIO
@login_manager.user_loader
def load_user(user_id):
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT * FROM usuarios WHERE id_usuario=%s", (user_id,))
    user = cursor.fetchone()
    cursor.close()

    if user:
        return Usuario(user[0], user[1], user[2])
    return None

# INICIO
@app.route('/')
def home():
    return redirect(url_for('login'))

# REGISTRO
@app.route('/registro', methods=['GET', 'POST'])
def registro():
    if request.method == 'POST':
        nombre = request.form['nombre']
        email = request.form['email']
        password = generate_password_hash(request.form['password'])

        cursor = mysql.connection.cursor()
        cursor.execute("INSERT INTO usuarios(nombre, email, password) VALUES(%s,%s,%s)",
                       (nombre, email, password))
        mysql.connection.commit()
        cursor.close()

        flash('Usuario registrado correctamente')
        return redirect(url_for('login'))

    return render_template('registro.html')

# LOGIN
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        cursor = mysql.connection.cursor()
        cursor.execute("SELECT * FROM usuarios WHERE email=%s", (email,))
        user = cursor.fetchone()
        cursor.close()

        if user and check_password_hash(user[3], password):
            usuario = Usuario(user[0], user[1], user[2])
            login_user(usuario)
            return redirect(url_for('dashboard'))
        else:
            flash('Correo o contraseña incorrectos')

    return render_template('login.html')

# DASHBOARD (CRUD)
@app.route('/dashboard')
@login_required
def dashboard():
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT * FROM usuarios")
    usuarios = cursor.fetchall()
    cursor.close()

    return render_template('dashboard.html', nombre=current_user.nombre, usuarios=usuarios)

# CREAR USUARIO DESDE DASHBOARD
@app.route('/crear_usuario', methods=['POST'])
@login_required
def crear_usuario():
    nombre = request.form['nombre']
    email = request.form['email']
    password = generate_password_hash(request.form['password'])

    cursor = mysql.connection.cursor()
    cursor.execute("INSERT INTO usuarios(nombre, email, password) VALUES(%s,%s,%s)",
                   (nombre, email, password))
    mysql.connection.commit()
    cursor.close()

    return redirect(url_for('dashboard'))

# ELIMINAR USUARIO
@app.route('/eliminar/<int:id>')
@login_required
def eliminar(id):
    cursor = mysql.connection.cursor()
    cursor.execute("DELETE FROM usuarios WHERE id_usuario=%s", (id,))
    mysql.connection.commit()
    cursor.close()

    return redirect(url_for('dashboard'))

# LOGOUT
@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True)