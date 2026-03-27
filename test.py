


# Mover el puntero al byte 10 desde el inicio
archivo.seek(10, 0)

# Leer los siguientes 20 caracteres
contenido_parcial = archivo.read(20)

# Mover al final y leer los últimos 50 bytes
archivo.seek(-50, 2)
ultimos_bytes = archivo.read(50)








archivo.seek(offset, desde_donde)