from extensions import db_s

class Comment(db_s.Model):
    id = db_s.Column(db_s.Integer, primary_key=True)
    texto = db_s.Column(db_s.Text, nullable=False)
    usuario_id = db_s.Column(db_s.Integer, db_s.ForeignKey('usuario.id'), nullable=False)
    post_id = db_s.Column(db_s.Integer, db_s.ForeignKey('post.id'), nullable=False)
