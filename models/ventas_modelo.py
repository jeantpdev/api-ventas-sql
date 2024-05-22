from flask import jsonify
from models.database.conexion_postgresql import *
import os 
class Modelo_Ventas():

    # Muestra todas las ventas
    def mostrar_ventas(self):
        try:
            connection = BD.conectar_postgres()

            cursor = connection.cursor()

            cursor.execute(f"SELECT * FROM {os.getenv('TABLE')} ORDER BY id DESC limit 5")

            column_names = [desc[0] for desc in cursor.description]

            rows = cursor.fetchall()

            results = []
            for row in rows:
                results.append(dict(zip(column_names, row)))

            return jsonify({"ventas": results}), 200
        except Exception as e:
            print("Ocurrió un error:", e)
            return jsonify({"mensaje": "Ocurrió un error al procesar la solicitud."}), 500
    
        finally:
            if connection:
                cursor.close()
                connection.close()

    # Muestra todas las ventas de agentes segun el lider de equipo
    def ventas_agentes_x_team_leader(self, lider_equipo):
        try:
            connection = BD.conectar_postgres()

            cursor = connection.cursor()

            cursor.execute(f"SELECT * FROM {os.getenv('TABLE')} WHERE lider_equipo LIKE '{lider_equipo}'")

            columnas = [desc[0] for desc in cursor.description]

            fila_agentes = cursor.fetchall()

            agentes = []
            for agente in fila_agentes:
                agentes.append(dict(zip(columnas, agente)))

            return jsonify({"lider_equipo": lider_equipo, "ventas": agentes}), 200
        except Exception as e:
            print("Ocurrió un error:", e)
            return jsonify({"mensaje": "Ocurrió un error al procesar la solicitud."}), 500
    
        finally:
            if connection:
                cursor.close()
                connection.close()
