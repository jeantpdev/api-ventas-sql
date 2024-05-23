from controllers.lideres_controlador import *
from flask import Blueprint
from flask_cors import cross_origin

Con_Lideres = Lideres_Controlador()

lideres = Blueprint('lideres', __name__)

@lideres.route('/top-lideres-mes/', methods=['GET'])
@cross_origin()
def get_top_lideres_mes():
   return Con_Lideres.get_top_lideres_mes()

@lideres.route('/agentes-pertenecientes/<lider_equipo>', methods=['GET'])
@cross_origin()
def get_agentes_pertenecientes(lider_equipo):
   return Con_Lideres.get_agentes_pertenecientes(lider_equipo)