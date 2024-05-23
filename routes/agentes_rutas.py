from controllers.agentes_controlador import *
from flask import Blueprint
from flask_cors import cross_origin

Con_Agentes = Agentes_Controlador()

agentes = Blueprint('agentes', __name__)

@agentes.route('/top-agentes-mes/', methods=['GET'])
@cross_origin()
def get_top_agentes_mes():
   return Con_Agentes.get_top_agentes_mes()

@agentes.route('/datos-personales/<cedula>', methods=['GET'])
@cross_origin()
def get_datos_personales(cedula):
   return Con_Agentes.get_datos_personales(cedula)