from models.user import Usuario

def obtener_usuarios():
    return Usuario.query.all()
