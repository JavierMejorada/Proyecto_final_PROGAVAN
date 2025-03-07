#Programa principal para creacion y acceder a rutas de la pagina 
#Usaremos flask para elaboracion de sevidor con nuestra api

from flask import Flask
from routes.routes import cargar_rutas
from extensions.extensions import db_s, jwt


#Creamos un objeto de tipo flask para ls metodos necesarios para nuestro servidor
app = Flask(__name__)
app.config['SECRET_KEY'] = 'pppolok' 
# 1.- Conectamos con mi base de datos en supabase pSQL
app.config['SQLALCHEMY_DATABASE_URI'] ='postgresql://postgres.ejolgythkfyrwedfvzlf:avan32J*@aws-0-us-west-1.pooler.supabase.com:6543/postgres'
#2.- Desactivacion del seguimiento de modificaciones
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
#3.- Agregamos la firma personal para nuestros tokens
app.config['JWT_SECRET_KEY']='vIsoctONeLeYelADAntErBo'

# Inicializar extensiones
db_s.init_app(app)
jwt.init_app(app)

# Cargar rutas
cargar_rutas(app)

# Ejecutar servidor
if __name__ == '__main__':
    app.run(port=8000, debug=True)
