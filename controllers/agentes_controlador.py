from models.agentes_modelo import *

Mod_Agentes = Modelo_Agentes()

class Agentes_Controlador():
    
    def get_top_agentes_mes(self):
        query = Mod_Agentes.top_agentes_mes()
        return query
