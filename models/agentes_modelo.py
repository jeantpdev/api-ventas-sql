from flask import jsonify
from models.database.conexion_postgresql import *
import os 

class Modelo_Agentes():

    # Muestra todas las ventas
    def top_agentes_mes(self):
        try:
            connection = BD.conectar_postgres()

            cursor = connection.cursor()

            cursor.execute(f"""
                WITH mes AS (SELECT DISTINCT * FROM {os.getenv('TABLE')}
                WHERE ventas.fecha_ingreso_venta 
                LIKE '%/03/2024')
                SELECT nombre_agente, COUNT(*) AS total_ventas 
                FROM mes 
                GROUP BY nombre_agente 
                ORDER BY total_ventas 
                DESC
                LIMIT 5;
                """)

            column_names = [desc[0] for desc in cursor.description]

            filas_agentes = cursor.fetchall()

            top_agentes = []
            for agente in filas_agentes:
                top_agentes.append(dict(zip(column_names, agente)))

            return jsonify({"top_agentes_mes": top_agentes}), 200
        except Exception as e:
            print("Ocurrió un error:", e)
            return jsonify({"mensaje": "Ocurrió un error al procesar la solicitud."}), 500
    
        finally:
            if connection:
                cursor.close()
                connection.close()