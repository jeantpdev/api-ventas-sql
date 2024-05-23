from flask import jsonify
from models.database.conexion_postgresql import *
import os 
class Modelo_Usuarios():

    def traer_usuarios(self):
        try:
            connection = BD.conectar_postgres()

            cursor = connection.cursor()

            cursor.execute(f"SELECT * FROM {os.getenv('TABLE_USERS')}")

            column_names = [desc[0] for desc in cursor.description]

            filas_usuarios = cursor.fetchall()

            usuarios = []
            for usuario in filas_usuarios:
                usuarios.append(dict(zip(column_names, usuario)))

            return jsonify({"usuarios": usuarios}), 200
        except Exception as e:
            print("Ocurrió un error:", e)
            return jsonify({"mensaje": "Ocurrió un error al procesar la solicitud."}), 500
    
        finally:
            if connection:
                cursor.close()
                connection.close()
