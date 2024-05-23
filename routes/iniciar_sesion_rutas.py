from controllers.iniciar_sesion_controlador import *
from flask import Blueprint
from flask_cors import cross_origin

Con_Inicio_Sesion = Inicio_Sesion_Controlador()

inicio_sesion = Blueprint('inicio_sesion', __name__)

@inicio_sesion.route('/iniciar-sesion/', methods=['POST'])
@cross_origin()
def post_iniciar_sesion():
   return Con_Inicio_Sesion.post_iniciar_sesion()
