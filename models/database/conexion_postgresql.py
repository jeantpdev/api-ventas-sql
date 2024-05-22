import psycopg2
import os 

class BD:

    def conectar_postgres():
        try:
            connection = psycopg2.connect(
                user = os.getenv('USER'),
                password = os.getenv('PASSWORD'),
                host = os.getenv('HOST'),
                port = os.getenv('PORT'),
                database = os.getenv('DATABASE')
            )

            return connection

        except (Exception, psycopg2.Error) as error:
            print("Error al conectar:", error)