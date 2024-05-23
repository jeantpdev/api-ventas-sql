from models.iniciar_sesion_modelo import *

Mod_Iniciar_Sesion = Iniciar_Sesion_Modelo()

class Inicio_Sesion_Controlador():
    
    def post_iniciar_sesion(self):
        query = Mod_Iniciar_Sesion.iniciar_sesion()
        return query

