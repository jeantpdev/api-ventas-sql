from models.usuarios_modelo import *

Mod_Usuarios = Modelo_Usuarios()

class Usuarios_Controlador():
    
    def get_traer_usuarios(self):
        query = Mod_Usuarios.traer_usuarios()
        return query