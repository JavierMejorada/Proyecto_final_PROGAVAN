from extensions.extensions import db_s

class Usuario(db_s.Model):
    id = db_s.Column(db_s.Integer, primary_key=True)
    nombre = db_s.Column(db_s.String(100), nullable=False)
    correo = db_s.Column(db_s.String(100), unique=True, nullable=False)
    password = db_s.Column(db_s.String(255), nullable=False)
