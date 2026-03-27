from datetime import datetime

def calcular_antiguedad(fecha_ingreso):
    """
    Calcula la antigüedad en años de un empleado
    comparando su fecha de ingreso con la fecha actual
    """
    fecha_actual = datetime.now()
    diferencia = fecha_actual - fecha_ingreso
    
    # Calcular años considerando si ya pasó el mes/día de aniversario este año
    años = fecha_actual.year - fecha_ingreso.year
    
    # Ajustar si aún no cumple años este año
    if (fecha_actual.month, fecha_actual.day) < (fecha_ingreso.month, fecha_ingreso.day):
        años -= 1
    
    return max(0, años)  # Evita negativos
