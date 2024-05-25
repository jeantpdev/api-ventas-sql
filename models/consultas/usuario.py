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

    def crear_usuario(datos_usuario):
        try:
            connection = BD.conectar_postgres()
            cursor = connection.cursor()

            cursor.execute(
                            """
                           INSERT INTO usuarios (usuario, 
                            contrasena, 
                            nombre, 
                            cedula, 
                            correo, 
                            lider_equipo, 
                            rol)
                            VALUES (%s, %s, %s, %s, %s, %s, %s)
                            RETURNING id_usuario
                            """,
                            datos_usuario
                            )
            id_usuario = cursor.fetchone()[0]

            connection.commit()

            return id_usuario
        
        except Exception as e:
            print("Ocurrió un error al crear el usuario:", e)
            return jsonify({"mensaje": "Ocurrió un error al procesar la solicitud."}), 500
    
        finally:
            if connection:
                cursor.close()
                connection.close()

