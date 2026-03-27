def determinar_beneficios(antiguedad):
    """
    Determina los beneficios según la antigüedad:
    - ≥ 5 años: Bono anual
    - ≥ 3 años: 5 días adicionales de vacaciones
    - < 3 años: Sin beneficios adicionales
    """
    if antiguedad >= 5:
        return "Bono anual"
    elif antiguedad >= 3:
        return "5 días adicionales de vacaciones"
    else:
        return "Sin beneficios adicionales"