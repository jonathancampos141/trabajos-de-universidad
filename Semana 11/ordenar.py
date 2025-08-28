def bubble_sort(fila):
    n = len(fila)
    for i in range(n):
        for j in range(0, n - i - 1):
            if fila[j] > fila[j + 1]:
                fila[j], fila[j + 1] = fila[j + 1], fila[j]  # Intercambiar


# Matriz de ejemplo 3x3
matriz = [
    [9, 2, 3],
    [4, 5, 6],
    [7, 8, 1]
]

print("Matriz original:")
for fila in matriz:
    print(fila)

fila_a_ordenar = 1  # Por ejemplo, ordenar la segunda fila (índice 1)
bubble_sort(matriz[fila_a_ordenar])

print("\nMatriz después de ordenar la fila:")
for fila in matriz:
    print(fila)
