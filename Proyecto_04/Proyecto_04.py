

# Registro de visitantes al Museo en París
def main():

    # REGISTRO DE VISITANTES POR SALA
    # *******************************************

    # Sala 1: Pedro, Carlos, Manuel, Laura
    sala1 = ["Pedro", "Carlos", "Manuel", "Laura"]
    
    # Sala 2: Juan, Elena, Pedro (Pedro ya estuvo en sala 1)
    sala2 = ["Juan", "Elena", "Pedro"]
    
    # Sala 3: Luis, Carlos (Carlos ya estuvo en sala 1)
    sala3 = ["Luis", "Carlos"]
    
    print("\n REGISTRO DE VISITANTES DEL MUSEO")
    print("********************************************")
    
    # Mostrar visitantes por sala
    print("Sala 1:", sala1)
    print(" Sala 2:", sala2)
    print(" Sala 3:", sala3)

    # OBTENER LISTA ÚNICA USANDO CONJUNTOS
    # *******************************************
    
    # Convertir listas a conjuntos para eliminar duplicados
    set_sala1 = set(sala1)
    set_sala2 = set(sala2)
    set_sala3 = set(sala3)
    
    # Unión de todos los conjuntos (todos los visitantes únicos)
    lista_unica = set_sala1 | set_sala2 | set_sala3
    
    print("\n LISTA ÚNICA DE VISITANTES")
    print("********************************************")
    
    # Mostrar resultado ordenado alfabéticamente
    for visitante in sorted(lista_unica):
        print(f"| {visitante}")
    
    print("********************************************")
    print(f"\nTotal de visitantes únicos: {len(lista_unica)}")
    
    # INFORMACIÓN ADICIONAL
    # *******************************************
    
    print("\n***** Estadísticas adicionales *****")
    print(f"Visitantes en Sala 1: {len(set_sala1)}")
    print(f"Visitantes en Sala 2: {len(set_sala2)}")
    print(f"Visitantes en Sala 3: {len(set_sala3)}")
    
    # Intersecciones (mismos visitantes en múltiples salas)
    inter_s1_s2 = set_sala1 & set_sala2
    inter_s1_s3 = set_sala1 & set_sala3
    
    if inter_s1_s2:
        print(f"\nVisitantes en Sala 1 y 2: {inter_s1_s2}")
    if inter_s1_s3:
        print(f"Visitantes en Sala 1 y 3: {inter_s1_s3}")

if __name__ == "__main__":
    main()