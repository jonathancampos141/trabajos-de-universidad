import random


def calcular_promedio_temperaturas(temperaturas, ciudades):
    """
    Calcula la temperatura promedio para cada ciudad dado un arreglo 3D de temperaturas.

    Parámetros:
    - temperaturas: lista 3D con datos de temperatura. Estructura: [ciudad][semana][día].
    - ciudades: lista con nombres de las ciudades.

    Retorna:
    - dict con la ciudad como clave y el promedio general de temperatura como valor.
    """
    promedios = {}
    for i, ciudad in enumerate(ciudades):
        # Obtener todas las temperaturas para esta ciudad (todas las semanas y días)
        temperaturas_ciudad = temperaturas[i]

        # Aplanar la lista para obtener todos los días en todas las semanas
        todas_temperaturas = [temp for semana in temperaturas_ciudad for temp in semana]

        # Calcular el promedio
        promedio = sum(todas_temperaturas) / len(todas_temperaturas)
        promedios[ciudad] = promedio

    return promedios


# Datos de ejemplo: 3 ciudades, 4 semanas, 7 días por semana
num_ciudades = 3
num_semanas = 4
num_dias = 7

ciudades = ["Quito", "Guayaquil", "Portovelo"]

# Generar datos aleatorios entre 15 y 30 grados para cada día, semana y ciudad
temperaturas = [[[random.randint(15, 30) for _ in range(num_dias)] for _ in range(num_semanas)] for _ in
                range(num_ciudades)]

# Mostrar datos generados (opcional)
print("Temperaturas generadas:")
for i, ciudad in enumerate(ciudades):
    print(f"\nCiudad: {ciudad}")
    for j in range(num_semanas):
        print(f" Semana {j + 1}: {temperaturas[i][j]}")

# Calcular promedios
promedios = calcular_promedio_temperaturas(temperaturas, ciudades)

print("\nPromedio de temperatura por ciudad (semana completa):")
for ciudad, promedio in promedios.items():
    print(f"{ciudad}: {promedio:.2f}°C")
