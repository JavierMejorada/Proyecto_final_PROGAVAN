from extensions import db_s

class Post(db_s.Model):
    id = db_s.Column(db_s.Integer, primary_key=True)
    titulo = db_s.Column(db_s.String(200), nullable=False)
    contenido = db_s.Column(db_s.Text, nullable=False)
    usuario_id = db_s.Column(db_s.Integer, db_s.ForeignKey('usuario.id'), nullable=False)
