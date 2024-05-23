from models.database.conexion_postgresql import *
from models.utils import *
from flask import jsonify

class Venta:
     
    # Si no tiene "valor retornar" retorna todos los datos del usuario
    def insertar_venta(datos_venta):
        try:
            connection = BD.conectar_postgres()
            cursor = connection.cursor()

            cursor.execute(
                """
                INSERT INTO venta (fk_id_cliente, fk_id_usuario, fk_id_calidad, fecha_ingreso, observaciones_venta, estado)
                VALUES (%s, %s, %s, %s, %s, %s)
                RETURNING id_venta
                """,
               datos_venta
            )
            id_venta = cursor.fetchone()[0]

            connection.commit()

            return id_venta

        except Exception as e:
            print("Ocurrió un error al insertar datos de venta:", e)
            # connection.rollback()
            return jsonify({"mensaje": "Ocurrió un error al procesar la solicitud."}), 500
    
        finally:
            if connection:
                cursor.close()
                connection.close()

