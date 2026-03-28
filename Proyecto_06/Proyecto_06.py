import json
import os

# ============================================
# FUNCIONES PARA MANEJO DE ARCHIVOS JSON
# ============================================

def escribir_archivo(nombre_archivo, datos):
    """
    Escribe datos en un archivo JSON.
    Modo 'w': escritura (sobrescribe si existe)
    """
    with open(nombre_archivo, 'w', encoding='utf-8') as archivo:
        json.dump(datos, archivo, indent=2, ensure_ascii=False)
    print(f"✓ Datos guardados exitosamente en '{nombre_archivo}'")

def leer_archivo(nombre_archivo):
    """
    Lee datos desde un archivo JSON.
    Retorna lista vacía si el archivo no existe.
    """
    try:
        with open(nombre_archivo, 'r', encoding='utf-8') as archivo:
            return json.load(archivo)
    except FileNotFoundError:
        print(f"⚠ Archivo '{nombre_archivo}' no encontrado. Se creará uno nuevo.")
        return []
    except json.JSONDecodeError:
        print(f"⚠ Error al decodificar '{nombre_archivo}'. Iniciando lista vacía.")
        return []

# ============================================
# FUNCIONES DEL SISTEMA
# ============================================

def agregar_libro(libros, archivo_libros):
    """Permite agregar un nuevo libro al sistema."""
    print("\n--- AGREGAR NUEVO LIBRO ---")
    titulo = input("Título del libro: ").strip()
    genero = input("Género: ").strip()
    try:
        anio = int(input("Año de publicación: "))
    except ValueError:
        print("× Error: El año debe ser un número.")
        return
    
    autor = input("Nombre del autor asociado: ").strip()
    
    libro = {
        "titulo": titulo,
        "genero": genero,
        "anio_publicacion": anio,
        "autor": autor
    }
    
    libros.append(libro)
    escribir_archivo(archivo_libros, libros)
    print(f"🕮 Libro '{titulo}' agregado exitosamente. ✔\n")

def agregar_autor(autores, archivo_autores):
    """Permite agregar un nuevo autor al sistema."""
    print("\n--- AGREGAR NUEVO AUTOR ---")
    nombre = input("Nombre del autor: ").strip()
    nacionalidad = input("Nacionalidad: ").strip()
    
    autor = {
        "nombre": nombre,
        "nacionalidad": nacionalidad
    }
    
    autores.append(autor)
    escribir_archivo(archivo_autores, autores)
    print(f"✍︎ Autor '{nombre}' agregado exitosamente. ✔\n")

def mostrar_informacion(libros, autores):
    """Muestra toda la información almacenada de forma legible."""
    print("\n" + "="*50)
    print("🏷  INFORMACIÓN DE LIBROS")
    print("="*50)
    
    if not libros:
        print("No hay libros registrados. :‹")
    else:
        for i, libro in enumerate(libros, 1):
            print(f"\n[{i}] Título: {libro['titulo']}")
            print(f"    Género: {libro['genero']}")
            print(f"    Año: {libro['anio_publicacion']}")
            print(f"    Autor: {libro['autor']}")
    
    print("\n" + "="*50)
    print("𓂃🖊  INFORMACIÓN DE AUTORES")
    print("="*50)
    
    if not autores:
        print("No hay autores registrados. :‹")
    else:
        for i, autor in enumerate(autores, 1):
            print(f"\n[{i}] Nombre: {autor['nombre']}")
            print(f"    Nacionalidad: {autor['nacionalidad']}")
    
    print("\n" + "="*50 + "\n")

# ============================================
# FUNCIÓN PRINCIPAL
# ============================================

def main():
    # Nombres de archivos para persistencia
    archivo_libros = "libros.json"
    archivo_autores = "autores.json"
    
    # Cargar datos existentes o inicializar listas vacías
    print("🔄 Cargando sistema...")
    libros = leer_archivo(archivo_libros)
    autores = leer_archivo(archivo_autores)
    print(f"   • {len(libros)} libro(s) cargado(s)")
    print(f"   • {len(autores)} autor(es) cargado(s)\n")
    
    # Menú principal
    while True:
        print("--- MENÚ PRINCIPAL ---")
        print("1. Agregar Libro")
        print("2. Agregar Autor")
        print("3. Mostrar Información")
        print("4. Salir")
        
        opcion = input("\nSeleccione una opción (1-4): ").strip()
        
        if opcion == '1':
            agregar_libro(libros, archivo_libros)
        elif opcion == '2':
            agregar_autor(autores, archivo_autores)
        elif opcion == '3':
            mostrar_informacion(libros, autores)
        elif opcion == '4':
            print("\n✌︎︎  ¡Gracias por usar nuestro sistema! ¡Hasta pronto!")
            break
        else:
            print("➝  Opción no válida. Por favor, ingrese un número del 1 al 4.\n")

# Punto de entrada del programa
if __name__ == "__main__":
    main()