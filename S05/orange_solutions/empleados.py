from collections import namedtuple
from datetime import datetime

# Definie estructura del empleado usando namedtuple de collections
Empleado = namedtuple('Empleado', ['nombre', 'salario', 'fecha_ingreso'])

def crear_empleado(nombre, salario, fecha_ingreso):
    """
    Crea un nuevo empleado con los datos proporcionados.
    fecha_ingreso debe ser un objeto datetime
    """
    return Empleado(nombre=nombre, salario=salario, fecha_ingreso=fecha_ingreso)

def mostrar_info_empleado(empleado):
    """Muestra la información básica del empleado"""
    print(f"Empleado: {empleado.nombre}")
    print(f"Salario: ${empleado.salario}")
    print(f"Fecha de Ingreso: {empleado.fecha_ingreso.strftime('%d/%m/%Y')}")