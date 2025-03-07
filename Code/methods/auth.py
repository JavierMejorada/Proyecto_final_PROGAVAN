from models.user import Usuario
from extensions.extensions import db_s
from werkzeug.security import generate_password_hash, check_password_hash
from flask import jsonify

def crear_cuenta(nombre, correo, password):
    if Usuario.query.filter_by(correo=correo).first():
        return {'status': 'error', 'message': 'Correo ya registrado'}

    hashed_password = generate_password_hash(password)
    nuevo_usuario = Usuario(nombre=nombre, correo=correo, password=hashed_password)
    db_s.session.add(nuevo_usuario)
    db_s.session.commit()

    return {'status': 'success', 'message': 'Cuenta creada exitosamente'}

def iniciar_sesion(correo, password):
    usuario = Usuario.query.filter_by(correo=correo).first()

    if not usuario or not check_password_hash(usuario.password, password):
        return {'status': 'error', 'message': 'Credenciales incorrectas'}

    token = 'FAKE_JWT_TOKEN'
    return {'status': 'success', 'token': token, 'usuario': usuario.nombre, 'correo': usuario.correo}