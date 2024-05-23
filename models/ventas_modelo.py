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
            
            datos_calidad = (request.json['llamada_realizada'], 
                            request.json['calidad_enviada'], 
                            request.json['observaciones_calidad'], 
                            request.json['audios_cargados'], 
                            request.json['verificacion'])

            try:
                #usuario_data = ('usuario1', 'password1', 'Nombre1', '123456789', 'email1@example.com', 'Lider1', 'Admin')
                # Datos de ejemplo para una sola entrada
                #usuario_data = ('usuario1', 'password1', 'Nombre1', '123456789', 'email1@example.com', 'Lider1', 'Admin')
                #cliente_data = ('Cliente1', 'DNI123456', '555-1234', '555-5678', 'cliente1@example.com', 'Direccion1', '1980-01-01', 'CUPS123', 'CUPS456', 'IBAN123456789', 'Contrato1', 'Potencia1', 'Peaje1', 'Mantenimiento1', 'Tipo1', 'Compania1')
                #calidad_data = (True, True, 'Observacion1', True, True)
                
                # Consultar datos del agente que realizo la venta mediante su cedula 
                cedula = Usuario.consultar_usuario(cedula, "cedula")
                # ID generado al crear el cliente
                id_cliente = Datos_Cliente.insertar_data_cliente(datos_cliente)
                # ID generado al crear la calidad
                id_calidad = Calidad.insertar_calidad(datos_calidad)

                print("La cedula del agente es:")
                print(cedula)
                print("El ID del cliente que se genero es:")
                print(id_cliente)
                print("El ID de la calidad que se genero es:")
                print(id_calidad)

                print("La cedula es")
                print(cedula[0])

                
                datos_venta = (id_cliente, 
                                cedula[0], 
                                id_calidad, 
                                request.json['fecha_ingreso'], 
                                request.json['observaciones_venta'],
                                "temporal")
                
                id_venta = Venta.insertar_venta(datos_venta)

                print("el id de la venta es:")
                print(id_venta)

            except Exception as e:
                # Si ocurre un error, revertir la transacción
                # connection.rollback()
                print("Error: ", e)


            return jsonify({"ventas": "results"}), 200
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