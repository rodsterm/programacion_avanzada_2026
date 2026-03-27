def calcular_precio(cantidad):
    """
    Calcula el precio unitario según la cantidad de llantas.
    - Menos de 5 llantas: $35,000 c/u
    - 5 a 10 llantas (inclusive): $40,000 c/u
    - Más de 10 llantas: $45,000 c/u
    """
    if cantidad < 5:           # 0-4 → 35.000
        return 35000
    elif 5 <= cantidad <= 10:  # 5-10 → 40.000
        return 40000
    else:                      # 11+ → 45.000
        return 45000

def formatear_numero(numero):
    """Formatea un número con separadores de miles y signo de peso."""
    return f"${numero:,}".replace(",", ".")

def main():
    print("=== Bienvenido a Rueda Fácil ===")
    
    # Validar entrada del número de clientes
    while True:
        try:
            num_clientes = int(input("Ingrese número de clientes: "))
            if num_clientes > 0:
                break
            else:
                print("Por favor ingrese un número mayor a cero.")
        except ValueError:
            print("Por favor ingrese un número válido.")
    
    # Procesar cada cliente
    for i in range(1, num_clientes + 1):
        print(f"\nCliente {i}:")
        
        # Validar cantidad de llantas
        while True:
            try:
                cantidad = int(input("  Cantidad de llantas: "))
                if cantidad > 0:
                    break
                else:
                    print("  La cantidad debe ser mayor a cero.")
            except ValueError:
                print("  Por favor ingrese un número válido.")
        
        # Calcular precios
        precio_unitario = calcular_precio(cantidad)
        total = cantidad * precio_unitario
        
        # Mostrar resultados
        print(f"  Precio unitario: {formatear_numero(precio_unitario)}")
        print(f"  Total a pagar: {formatear_numero(total)}")

if __name__ == "__main__":
    main()