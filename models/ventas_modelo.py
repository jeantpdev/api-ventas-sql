from flask import jsonify, request
from models.database.conexion_postgresql import *
from models.consultas.usuario import *
from models.consultas.datos_cliente import *
from models.consultas.calidad import *
from models.consultas.venta import *
import os 
class Modelo_Ventas():

    # Muestra todas las ventas
    def crear_venta(self):
        try:
            connection = BD.conectar_postgres()

            cursor = connection.cursor()
            cedula = request.json["cedula"]

            datos_cliente = (request.json['nombre'], 
                            request.json['dni'], 
                            request.json['telefono'], 
                            request.json['telefono_fijo'], 
                            request.json['correo'], 
                            request.json['direccion'], 
                            request.json['fecha_nacimiento'], 
                            request.json['cups_luz'], 
                            request.json['cups_gas'], 
                            request.json['iban'], 
                            request.json['numero_contrato'], 
                            request.json['potencia'], 
                            request.json['peaje_gas'], 
                            request.json['mantenimiento'], 
                            request.json['tipo_mantenimiento'], 
                            request.json['compania'])
            
            datos_calidad = (bool(request.json['llamada_realizada']), 
                            bool(request.json['calidad_enviada']), 
                            request.json['observaciones_calidad'], 
                            bool(request.json['audios_cargados']), 
                            bool(request.json['verificacion']))

            try:
                
                # Consultar datos del agente que realizo la venta mediante su cedula 
                id_usuario = Usuario.consultar_usuario(cedula, "id_usuario")
                print("ID de usuario obtenido", id_usuario)

                id_cliente = Datos_Cliente.insertar_data_cliente(datos_cliente)
                print("ID del cliente generado", id_cliente)

                id_calidad = Calidad.insertar_calidad(datos_calidad)
                print("ID del registro calidad generado", id_calidad)

                datos_venta = (id_cliente, 
                                id_usuario, 
                                id_calidad, 
                                request.json['fecha_ingreso'], 
                                request.json['observaciones_venta'],
                                "temporal")
                
                id_venta = Venta.insertar_venta(datos_venta)

                print("ID de venta generado:", id_venta)

            except Exception as e:
                connection.rollback()
                print("Error: ", e)

            return jsonify({"status": "OK"}), 200
        except Exception as e:
            print("Ocurrió un error:", e)
            return jsonify({"mensaje": "Ocurrió un error al procesar la solicitud."}), 500
    
        finally:
            if connection:
                cursor.close()
                connection.close()

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
    
    def ventas_agente(self, cedula):
        try:
            connection = BD.conectar_postgres()

            cursor = connection.cursor()

            id_usuario = Usuario.consultar_usuario(cedula, "id_usuario")

            cursor.execute(f"""
                SELECT 
                    Venta.id_venta,
                    datos_cliente.nombre AS nombre_cliente,
                    datos_cliente.dni,
                    datos_cliente.telefono,
                    datos_cliente.correo AS correo,
                    Usuarios.nombre AS agente,
                    Calidad.llamada_realizada,
                    Calidad.calidad_enviada,
                    Calidad.verificacion AS verificacion_calidad,
                    Calidad.observaciones AS observaciones_calidad,
                    Venta.fecha_ingreso,
                    Venta.observaciones_venta,
                    Venta.estado
                FROM 
                    Venta
                JOIN 
                    datos_cliente ON Venta.fk_id_cliente = datos_cliente.id_cliente
                JOIN 
                    Usuarios ON Venta.fk_id_usuario = Usuarios.id_usuario
                JOIN 
                    Calidad ON Venta.fk_id_calidad = Calidad.id_calidad
                WHERE 
                    Venta.fk_id_usuario = {id_usuario};
                           """)

            column_names = [desc[0] for desc in cursor.description]

            fila_ventas = cursor.fetchall()

            ventas_agente = []
            for venta in fila_ventas:
                ventas_agente.append(dict(zip(column_names, venta)))

            return jsonify({"ventas_agente": ventas_agente}), 200
        except Exception as e:
            print("Ocurrió un error:", e)
            return jsonify({"mensaje": "Ocurrió un error al procesar la solicitud."}), 500
    
        finally:
            if connection:
                cursor.close()
                connection.close()