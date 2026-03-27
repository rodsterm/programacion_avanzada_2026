def gestionar_inventario():
    while True:
        try:
            existencia = int(input("Ingrese cantidad actual de frutas/verduras: "))
            vendidos = int(input("Ingrese cantidad vendida durante el día: "))

            if existencia < 0 or vendidos < 0:
                raise ValueError("Las cantidades no pueden ser negativas.")
            if vendidos > existencia:
                raise ValueError("La cantidad vendida no puede exceder la existente.")

            inventario_final = existencia - vendidos
            print(f"Inventario actualizado: {inventario_final} unidades restantes.")
            break

        except ValueError as e:
            print(f"Error: {e}. Por favor, ingrese valores válidos.\n")

# Ejecutar programa
gestionar_inventario()