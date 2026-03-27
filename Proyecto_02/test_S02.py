import math

# Función recursiva para calcular el factorial (ejemplo de recursividad)
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

# Función para calcular el descuento en licencias
def calcular_descuento(cantidad, precio_base=100000):
    if cantidad >= 5:
        descuento = 0.30
    elif cantidad >= 3:
        descuento = 0.20
    else:
        descuento = 0

    total = cantidad * precio_base * (1 - descuento)
    return total, descuento

# Función para calcular el volumen de una esfera
def volumen_esfera(radio):
    volumen = (4/3) * math.pi * (radio ** 3)
    return volumen

# Función principal con menú interactivo
def main():
    while True:
        print("\n--- Menú de Opciones ---")
        print("1. Calcular descuento en compras de software")
        print("2. Calcular volumen de una esfera")
        print("3. Salir del programa")
        
        opcion = input("Seleccione una opción (1, 2 o 3): ")

        if opcion == '1':
            try:
                cantidad = int(input("Ingrese la cantidad de licencias: "))
                if cantidad <= 0:
                    print("❌ La cantidad debe ser mayor a 0.")
                    continue
                total, descuento = calcular_descuento(cantidad)
                print(f"✅ Total a pagar: ${total:,.0f}")
                print(f"📉 Descuento aplicado: {int(descuento * 100)}%")
            except ValueError:
                print("❌ Ingrese un número válido.")

        elif opcion == '2':
            try:
                radio = float(input("Ingrese el radio de la esfera: "))
                if radio <= 0:
                    print("❌ El radio debe ser mayor a 0.")
                    continue
                volumen = volumen_esfera(radio)
                print(f"✅ El volumen de la esfera es: {volumen:.2f} unidades cúbicas")
            except ValueError:
                print("❌ Ingrese un número válido.")

        elif opcion == '3':
            print("👋 ¡Hasta luego! Gracias por usar el programa.")
            break

        else:
            print("❌ Opción no válida. Por favor, seleccione 1, 2 o 3.")

# Ejecutar el programa
if __name__ == "__main__":
    main()