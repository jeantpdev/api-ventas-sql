class Utilidades:

    def respuesta_consulta(cursor):
        nombres_columnas = [desc[0] for desc in cursor.description]

        filas_consulta = cursor.fetchall()

        consulta = []
        for usuario in filas_consulta:
            consulta.append(dict(zip(nombres_columnas, usuario)))

        return consulta