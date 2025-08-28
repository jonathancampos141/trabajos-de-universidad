def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                # Intercambiar
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

def ordenar_fila(matriz, fila):
    # Copiar la fila para no modificar la matriz original directamente
    fila_a_ordenar = matriz[fila][:]
    bubble_sort(fila_a_ordenar)
    # Crear una copia de la matriz para no modificar la original
    matriz_ordenada = [row[:] for row in matriz]
    matriz_ordenada[fila] = fila_a_ordenar
    return matriz_ordenada

def imprimir_matriz(matriz):
    for fila in matriz:
        print(fila)

def main():
    matriz = [
        [12, 5, 9],
        [7, 3, 14],
        [8, 11, 6]
    ]

    print("Matriz original:")
    imprimir_matriz(matriz)

    fila_a_ordenar = 1  # Por ejemplo, ordenar la segunda fila (índice 1)
    matriz_ordenada = ordenar_fila(matriz, fila_a_ordenar)

    print(f"\nMatriz con la fila {fila_a_ordenar} ordenada:")
    imprimir_matriz(matriz_ordenada)

if __name__ == "__main__":
    main()


