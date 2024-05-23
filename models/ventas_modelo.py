from flask import jsonify
from models.database.conexion_postgresql import *
import os 
class Modelo_Ventas():

    # Muestra todas las ventas
    def mostrar_ventas(self):
        try:
            connection = BD.conectar_postgres()

            cursor = connection.cursor()

            cursor.execute(f"SELECT * FROM {os.getenv('TABLE')} ORDER BY id DESC limit 800")

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

    def ventas_mes_actual(self):
        try:
            connection = BD.conectar_postgres()

            cursor = connection.cursor()

            cursor.execute(f"SELECT * FROM {os.getenv('TABLE')} v WHERE v.fecha_ingreso_venta LIKE '%/03/2024';")

            column_names = [desc[0] for desc in cursor.description]

            fila_ventas = cursor.fetchall()

            ventas_mes_actual = []
            for venta in fila_ventas:
                ventas_mes_actual.append(dict(zip(column_names, venta)))

            return jsonify({"ventas_mes_actual": ventas_mes_actual}), 200
        except Exception as e:
            print("Ocurrió un error:", e)
            return jsonify({"mensaje": "Ocurrió un error al procesar la solicitud."}), 500
    
        finally:
            if connection:
                cursor.close()
                connection.close()

    def ventas_ultimo_trimestre(self):
        try:
            connection = BD.conectar_postgres()

            cursor = connection.cursor()

            cursor.execute(f"""SELECT *
                            FROM {os.getenv('TABLE')}
                            WHERE TO_DATE(fecha_ingreso_venta, 'DD/MM/YYYY') >= (CURRENT_DATE - INTERVAL '3 months')
                            ORDER BY id DESC;
                           """)

            column_names = [desc[0] for desc in cursor.description]

            fila_ventas = cursor.fetchall()

            ventas_ultimo_trimestre = []
            for venta in fila_ventas:
                ventas_ultimo_trimestre.append(dict(zip(column_names, venta)))

            return jsonify({"ventas_ultimo_trimestre": ventas_ultimo_trimestre}), 200
        except Exception as e:
            print("Ocurrió un error:", e)
            return jsonify({"mensaje": "Ocurrió un error al procesar la solicitud."}), 500
    
        finally:
            if connection:
                cursor.close()
                connection.close()

    def ventas_dia_actual(self):
        try:
            connection = BD.conectar_postgres()

            cursor = connection.cursor()

            cursor.execute(f"select * from {os.getenv('TABLE')} v where v.fecha_ingreso_venta like '22/02/2024'")

            column_names = [desc[0] for desc in cursor.description]

            fila_ventas = cursor.fetchall()

            ventas_dia_actual = []
            for venta in fila_ventas:
                ventas_dia_actual.append(dict(zip(column_names, venta)))

            return jsonify({"ventas_dia_actual": ventas_dia_actual}), 200
        except Exception as e:
            print("Ocurrió un error:", e)
            return jsonify({"mensaje": "Ocurrió un error al procesar la solicitud."}), 500
    
        finally:
            if connection:
                cursor.close()
                connection.close()