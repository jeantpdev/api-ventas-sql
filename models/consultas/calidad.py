from models.database.conexion_postgresql import *
from models.utils import *
from flask import jsonify

class Calidad:
     
    # Si no tiene "valor retornar" retorna todos los datos del usuario
    def insertar_calidad(datos_calidad):
        try:
            connection = BD.conectar_postgres()
            cursor = connection.cursor()

            cursor.execute(
                """
                INSERT INTO calidad (llamada_realizada, calidad_enviada, observaciones, audios_cargados, verificacion)
                VALUES (%s, %s, %s, %s, %s)
                RETURNING id_calidad
                """,
               datos_calidad
            )
            id_calidad = cursor.fetchone()[0]

            connection.commit()

            return id_calidad

        except Exception as e:
            print("Ocurrió un error:", e)
            # connection.rollback()
            return jsonify({"mensaje": "Ocurrió un error al procesar la solicitud."}), 500
    
        finally:
            if connection:
                cursor.close()
                connection.close()

