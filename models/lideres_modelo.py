from flask import jsonify
from models.database.conexion_postgresql import *
import os 

class Modelo_Lideres():

    # Muestra todas las ventas
    def top_lideres_mes(self):
        try:
            connection = BD.conectar_postgres()

            cursor = connection.cursor()

            cursor.execute(f"""
                WITH mes AS (SELECT DISTINCT  * FROM {os.getenv('TABLE')}
                WHERE  ventas.fecha_ingreso_venta 
                LIKE  '%/03/2024')
                SELECT  lider_equipo, COUNT(*) AS total_ventas 
                FROM mes 
                GROUP BY lider_equipo
                ORDER BY total_ventas 
                DESC;
                """)

            column_names = [desc[0] for desc in cursor.description]

            rows = cursor.fetchall()

            results = []
            for row in rows:
                results.append(dict(zip(column_names, row)))

            return jsonify({"top_lideres_mes": results}), 200
        except Exception as e:
            print("Ocurrió un error:", e)
            return jsonify({"mensaje": "Ocurrió un error al procesar la solicitud."}), 500
    
        finally:
            if connection:
                cursor.close()
                connection.close()

    # Muestra todas las ventas
    def agentes_pertenecientes(self, lider_equipo):
        try:
            connection = BD.conectar_postgres()

            cursor = connection.cursor()

            cursor.execute(f"SELECT DISTINCT nombre_agente, lider_equipo FROM {os.getenv('TABLE')} WHERE lider_equipo LIKE '{lider_equipo}';")

            column_names = [desc[0] for desc in cursor.description]

            filas_agentes = cursor.fetchall()

            agentes = []
            for agente in filas_agentes:
                agentes.append(dict(zip(column_names, agente)))

            return jsonify({"lider_equipo": lider_equipo, "agentes": agentes}), 200
        except Exception as e:
            print("Ocurrió un error:", e)
            return jsonify({"mensaje": "Ocurrió un error al procesar la solicitud."}), 500
    
        finally:
            if connection:
                cursor.close()
                connection.close()