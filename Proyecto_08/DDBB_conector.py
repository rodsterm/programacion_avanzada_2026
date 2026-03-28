import mysql.connector

config = {
    'user': 'root',           # Usuario de MySQL
    'password': '',           # Contraseña
    'host': 'localhost',      # Servidor
    'database': 'semana8'     # Base de datos
}

conexion = mysql.connector.connect(**config)

cursor = conexion.cursor()

cursor.close()
conexion.close()

