from flask import Flask, render_template, request, redirect, url_for, make_response
from methods.auth import crear_cuenta, iniciar_sesion
from methods.queries import obtener_usuarios
from flask import flash, get_flashed_messages
from models.user import Usuario

def cargar_rutas(app):

    @app.route('/')
    def pagina():
        return render_template('index.html')

    @app.route('/login')
    def login():
        return render_template('login.html')

    @app.route('/register', methods=['GET', 'POST'])
    def signup():
        if request.method == 'POST':
            # Lógica para manejar el registro
            nombre = request.form.get('name')
            correo = request.form.get('email')
            password = request.form.get('password')

            respuesta = crear_cuenta(nombre, correo, password)

            if respuesta['status'] == 'error':
                return redirect(url_for('signup', status=respuesta['status']))

            return redirect(url_for('pagina'))

        # Si es una solicitud GET, simplemente renderiza la plantilla
        return render_template('register.html')

    @app.route('/manipulacion', methods=['POST'])
    def manipular_datos():
        correo = request.form.get('email')
        password = request.form.get('password')
        respuesta = iniciar_sesion(correo, password)

        if respuesta['status'] == 'error':
            return redirect(url_for('login', status=respuesta['status']))
        
        flash('¡Bienvenido!', 'success')

        res = make_response(redirect(url_for('dashboard')))
        res.set_cookie('user_email', correo, secure=True, max_age=3600) 
        res.set_cookie('access_token', respuesta['token'], secure=True, max_age=3600)
        return res

    @app.route('/datos_crear_cuenta', methods=['POST'])
    def obtener_datos_cuenta():
        nombre = request.form.get('name')
        correo = request.form.get('email')
        password = request.form.get('password')

        respuesta = crear_cuenta(nombre, correo, password)

        if respuesta['status'] == 'error':
            return redirect(url_for('signup', status=respuesta['status']))

        return redirect(url_for('pagina'))

    @app.route('/dashboard')
    def dashboard():
        correo_usuario = request.cookies.get('user_email')
        if not correo_usuario:
            return redirect(url_for('login'))
        usuario = Usuario.query.filter_by(correo=correo_usuario).first()
    
        return render_template('dashboard.html', Nombre=usuario.nombre, Correo=correo_usuario)
    @app.route('/logout')
    def logout():
        flash('¡Hasta pronto!', 'info')
        respuesta = make_response(redirect(url_for('pagina')))  
        respuesta.set_cookie('access_token', '', max_age=0)  
        return respuesta
    @app.route('/comprar')
    def comprar():
        correo_usuario = request.cookies.get('user_email')
        if not correo_usuario:
            return redirect(url_for('login'))

        usuario = Usuario.query.filter_by(correo=correo_usuario).first()
        if not usuario:
            return redirect(url_for('login'))

        return render_template('comprar.html', Nombre=usuario.nombre)