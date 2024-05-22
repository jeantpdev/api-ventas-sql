from flask import Flask
from flask_cors import CORS
#from flask_jwt_extended import JWTManager, create_access_token, jwt_required
from dotenv import load_dotenv

load_dotenv()
from routes.ventas_rutas import *

app = Flask(__name__)
cors = CORS(app, resources={r"/*": {"origins": "*"}})

# GENERALES
app.register_blueprint(todo)

#Pagina de error
def pagina_no_encontrada(error):
    return "<h1>La pagina a la que intentas acceder no existe...</h1>"

if __name__=="__main__":
    app.register_error_handler(404 , pagina_no_encontrada)
    app.run(host="0.0.0.0",port = 5700, debug=True)