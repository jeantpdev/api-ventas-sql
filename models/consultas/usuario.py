from models.database.conexion_postgresql import *
from models.utils import *
from flask import jsonify

class Usuario:
     
    # Si no tiene "valor retornar" retorna todos los datos del usuario
    def consultar_usuario(cedula_usuario, valor_retornar = None):
        try:
            connection = BD.conectar_postgres()
            cursor = connection.cursor()

            cursor.execute(f"SELECT * FROM public.usuarios WHERE cedula = '{cedula_usuario}'")

            datos_usuario = Utilidades.respuesta_consulta(cursor)
            
            if valor_retornar:
                return datos_usuario[0][valor_retornar]

            return datos_usuario
        
        except Exception as e:
            print("Ocurrió un error:", e)
            return jsonify({"mensaje": "Ocurrió un error al procesar la solicitud."}), 500
    
        finally:
            if connection:
                cursor.close()
                connection.close()

