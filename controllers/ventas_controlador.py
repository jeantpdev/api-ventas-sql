from models.ventas_modelo import *

Mod_Ventas = Modelo_Ventas()

class Ventas_Controlador():
    
    def get_ventas(self):
        query = Mod_Ventas.mostrar_ventas()
        return query
    
    def get_ventas_agentes_x_team_leader(self, lider_equipo):
        query = Mod_Ventas.ventas_agentes_x_team_leader(lider_equipo)
        return query