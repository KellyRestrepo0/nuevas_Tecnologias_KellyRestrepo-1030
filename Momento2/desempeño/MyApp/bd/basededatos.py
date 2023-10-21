import mysql.connector

conexion = mysql.connector.connect(
            host='localhost',
            user='root',
            password='',
            db='Base_prueba'
        )

conexion.close()s

