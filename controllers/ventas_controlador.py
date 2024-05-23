from models.ventas_modelo import *

Mod_Ventas = Modelo_Ventas()

class Ventas_Controlador():
    
    def get_ventas(self):
        query = Mod_Ventas.mostrar_ventas()
        return query
    
    def get_ventas_agentes_x_team_leader(self, lider_equipo):
        query = Mod_Ventas.ventas_agentes_x_team_leader(lider_equipo)
        return query
    
    def get_ventas_mes_actual(self):
        query = Mod_Ventas.ventas_mes_actual()
        return query

    def get_ventas_ultimo_trimestre(self):
        query = Mod_Ventas.ventas_ultimo_trimestre()
        return query
    
    def get_ventas_dia_actual(self):
        query = Mod_Ventas.ventas_dia_actual()
        return query

    def post_venta(self):
        query = Mod_Ventas.crear_venta()
        return query