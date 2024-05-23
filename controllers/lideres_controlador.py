from models.lideres_modelo import *

Mod_Lideres = Modelo_Lideres()

class Lideres_Controlador():
    
    def get_top_lideres_mes(self):
        query = Mod_Lideres.top_lideres_mes()
        return query
    
    def get_agentes_pertenecientes(self, lider_equipo):
        query = Mod_Lideres.agentes_pertenecientes(lider_equipo)
        return query

