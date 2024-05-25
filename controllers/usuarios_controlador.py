from models.usuarios_modelo import *

Mod_Usuarios = Modelo_Usuarios()

class Usuarios_Controlador():
    
    def get_traer_usuarios(self):
        query = Mod_Usuarios.traer_usuarios()
        return query
    
    def post_crear_usuario(self):
        query = Mod_Usuarios.crear_usuario()
        return query