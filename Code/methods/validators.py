import re

def validar_correo(correo):
    return re.match(r"[^@]+@[^@]+\.[^@]+", correo) is not None
