# Definir matriz
matriz1 = [
    [10, 24, 30],
    [25, 11, 40],
    [19, 60, 98]
]

matriz2 = [
    [28, 74, 18],
    [54, 19, 89],
    [64, 85, 34]
]


# Función buscar
def buscar_valor(matriz, valor):
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j] == valor:
                return (i, j)
    return None


# Función para ordenar una fila usando Bubble Sort
def ordenar_fila(matriz, fila):
    n = len(matriz[fila])
    for i in range(n):
        for j in range(0, n - i - 1):
            if matriz[fila][j] > matriz[fila][j + 1]:
                matriz[fila][j], matriz[fila][j + 1] = matriz[fila][j + 1], matriz[fila][j]


# Valor a buscar
valor_a_buscar = 30

posicion1 = buscar_valor(matriz1, valor_a_buscar)
posicion2 = buscar_valor(matriz2, valor_a_buscar)

# Mostrar el resultado
if posicion1:
    print(f"Valor {valor_a_buscar} encontrado en la primera matriz en la posición {posicion1}")
elif posicion2:
    print(f"Valor {valor_a_buscar} encontrado en la segunda matriz en la posición {posicion2}")
else:
    print(f"Valor {valor_a_buscar} no encontrado en ninguna de las matrices")

# Mostrar la matriz original
print("Matriz original:")
for fila in matriz1:
    print(fila)

# Ordenar la segunda fila de la primera matriz
ordenar_fila(matriz1, 1)

# Mostrar la matriz con la fila ordenada
print("\nMatriz con la segunda fila ordenada:")
for fila in matriz1:
    print(fila)