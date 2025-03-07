from flask import jsonify

def error_404(e):
    return jsonify({'error': 'Página no encontrada'}), 404

def error_500(e):
    return jsonify({'error': 'Error interno del servidor'}), 500
