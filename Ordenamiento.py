# Solicitar al usuario ingresar una serie de números separados por espacios
entrada = input("Ingresa una serie de números separados por espacios: ")

# Dividir la entrada en una lista de números
numeros = [float(numero) for numero in entrada.split()]

# Implementar el algoritmo de ordenamiento de selección
n = len(numeros)
for i in range(n):
    # Encontrar el índice del elemento mínimo en el resto de la lista
    min_index = i
    for j in range(i + 1, n):
        if numeros[j] < numeros[min_index]:
            min_index = j
    
    # Intercambiar el elemento actual con el mínimo encontrado
    numeros[i], numeros[min_index] = numeros[min_index], numeros[i]

# Mostrar la lista ordenada
print("Lista ordenada en orden ascendente:")
for numero in numeros:
    print(numero, end=" ")
