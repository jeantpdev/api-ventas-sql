from flask import jsonify, request
from models.database.conexion_postgresql import *
from flask_jwt_extended import create_access_token, jwt_required

import os 
class Iniciar_Sesion_Modelo():

    # Muestra todas las ventas
    def iniciar_sesion(self):
        try:

            usuario = request.json['usuario']
            contrasena = request.json['contrasena']
            connection = BD.conectar_postgres()

            cursor = connection.cursor()

            cursor.execute(f"SELECT rol, cedula FROM public.agentes WHERE usuario = '{usuario}' AND contrasena = '{contrasena}'")

            column_names = [desc[0] for desc in cursor.description]

            rows = cursor.fetchall()

            results = []
            for row in rows:
                results.append(dict(zip(column_names, row)))
            
            if len(results) == 0:
                print("No existe el usuario")
                return jsonify({"msg": "Credenciales inválidas"}), 401
            
            cedula = results[0]['cedula']
            rol = results[0]['rol']
            access_token = create_access_token(identity = usuario)
        
            return jsonify({"access_token": access_token, "acceso": "AUTORIZADO", "cedula": cedula, "rol": rol}), 200
        except Exception as e:
            print("Ocurrió un error:", e)
            return jsonify({"mensaje": "Ocurrió un error al procesar la solicitud."}), 500
    
        finally:
            if connection:
                cursor.close()

                connection.close()
