from controllers.ventas_controlador import *
from flask import Blueprint
from flask_cors import cross_origin

Con_Ventas = Ventas_Controlador()

ventas = Blueprint('ventas', __name__)

@ventas.route('/mostrar-ventas/', methods=['GET'])
@cross_origin()
def get_ventas():
   return Con_Ventas.get_ventas()

@ventas.route('/ventas-agente-por-lider/<lider_equipo>', methods=['GET'])
@cross_origin()
def get_ventas_agentes_x_team_leader(lider_equipo):
   return Con_Ventas.get_ventas_agentes_x_team_leader(lider_equipo)

@ventas.route('/ventas-mes-actual/', methods=['GET'])
@cross_origin()
def get_ventas_mes_actual():
   return Con_Ventas.get_ventas_mes_actual()

@ventas.route('/ventas-ultimo-trimestre/', methods=['GET'])
@cross_origin()
def get_ventas_ultimo_trimestre():
   return Con_Ventas.get_ventas_ultimo_trimestre()

@ventas.route('/ventas-dia-actual/', methods=['GET'])
@cross_origin()
def get_ventas_dia_actual():
   return Con_Ventas.get_ventas_dia_actual()

@ventas.route('/crear-venta/', methods=['POST'])
@cross_origin()
def post_venta():
   return Con_Ventas.post_venta()

@ventas.route('/venta-agente/<cedula>', methods=['GET'])
@cross_origin()
def get_venta_agente(cedula):
   return Con_Ventas.get_venta_agente(cedula)