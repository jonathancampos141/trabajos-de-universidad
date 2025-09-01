import random

# Definir las dimensiones de la matriz
ciudades = ["Zaruma", "Paccha", "Portovelo"]
num_ciudades = len(ciudades)
num_semanas = 4
num_dias = 7

# Crear la matriz 3D con temperaturas aleatorias (entre 15 y 30 grados Celsius)
temperaturas = [[[random.randint(15, 30) for _ in range(num_dias)] for _ in range(num_semanas)] for _ in range(num_ciudades)]

# Imprimir la matriz para visualización
print("Matriz 3D de Temperaturas:")
for i in range(num_ciudades):
    print(f"\n--- {ciudades[i]} ---")
    for j in range(num_semanas):
        print(f"Semana {j+1}: {temperaturas[i][j]}")

# Calcular y mostrar el promedio de temperaturas para cada ciudad por semana
print("\n--- Promedio de Temperaturas por Ciudad y Semana ---")
for i in range(num_ciudades):
    print(f"\nCiudad: {ciudades[i]}")
    for j in range(num_semanas):
        # Utilizar la función sum() para sumar todos los elementos de la sublista y len() para contar cuántos elementos hay
        promedio_semanal = sum(temperaturas[i][j]) / len(temperaturas[i][j])
        print(f"  Semana {j+1}: {promedio_semanal:.2f}°C")