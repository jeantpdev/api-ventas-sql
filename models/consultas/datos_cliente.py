from models.database.conexion_postgresql import *
from models.utils import *
from flask import jsonify

class Datos_Cliente:
     
    # Si no tiene "valor retornar" retorna todos los datos del usuario
    def insertar_data_cliente(datos_cliente):
        try:
            connection = BD.conectar_postgres()
            cursor = connection.cursor()

            cursor.execute(
                """
                INSERT INTO datos_cliente (nombre, 
                dni, 
                telefono, 
                telefono_fijo, 
                correo, 
                direccion, 
                fecha_nacimiento, 
                cups_luz, 
                cups_gas, 
                iban, 
                numero_contrato, 
                potencia, 
                peaje_gas, 
                mantenimiento, 
                tipo_mantenimiento, 
                compania)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
                RETURNING id_cliente
                """,
               datos_cliente
            )
            id_cliente = cursor.fetchone()[0]

            connection.commit()

            return id_cliente

        except Exception as e:
            print("Ocurrió un error en insertar data cliente:", e)
            # connection.rollback()
            return jsonify({"mensaje": "Ocurrió un error al procesar la solicitud."}), 500
    
        finally:
            if connection:
                cursor.close()
                connection.close()

