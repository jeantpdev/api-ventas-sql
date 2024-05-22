from controllers.ventas_controlador import *
from flask import Blueprint
from flask_cors import cross_origin

Con_Ventas = Ventas_Controlador()

todo = Blueprint('todo', __name__)

@todo.route('/mostrar-ventas/', methods=['GET'])
@cross_origin()
def get_ventas():
   return Con_Ventas.get_ventas()

@todo.route('/ventas-agente-por-lider/<lider_equipo>', methods=['GET'])
@cross_origin()
def get_ventas_agentes_x_team_leader(lider_equipo):
   return Con_Ventas.get_ventas_agentes_x_team_leader(lider_equipo)