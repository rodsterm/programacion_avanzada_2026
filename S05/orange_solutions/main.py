from datetime import datetime
from empleados import crear_empleado, mostrar_info_empleado
from calculos import calcular_antiguedad
from beneficios import determinar_beneficios

def main():
    # Datos de prueba según enunciado de la evaluación
    nombre_empleado = "María García"
    salario_empleado = 60000
    fecha_ingreso_empleado = datetime(2019, 3, 20)
    
    # Crear empleado
    empleado = crear_empleado(nombre_empleado, salario_empleado, fecha_ingreso_empleado)
    
    # Calcular antigüedad
    antiguedad = calcular_antiguedad(fecha_ingreso_empleado)
    
    # Determinar beneficios
    beneficios = determinar_beneficios(antiguedad)
    
    # Mostrar resultados
    print("=" * 50)
    print("SISTEMA DE GESTIÓN DE EMPLEADOS - ORANGE SOLUTIONS")
    print("=" * 50)
    mostrar_info_empleado(empleado)
    print(f"Antigüedad: {antiguedad} años")
    print(f"Beneficios Asignados: {beneficios}")
    print("=" * 50)

if __name__ == "__main__":
    main()
    