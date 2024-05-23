from controllers.usuarios_controlador import *
from flask import Blueprint
from flask_cors import cross_origin

Con_Usuario = Usuarios_Controlador()

usuarios = Blueprint('usuarios', __name__)

@usuarios.route('/traer-usuarios/', methods=['GET'])
@cross_origin()
def get_traer_usuarios():
   return Con_Usuario.get_traer_usuarios()
