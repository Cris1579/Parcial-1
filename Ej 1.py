# Obtener determinante de una matriz 3x3
# Con sus elementos aleatorios (De 5 a 10)
import numpy as np

# Para generar una matriz de 3x3 con elementos aleatorios
matriz = np.random.randint(5, 10, (3, 3))
print("Matriz:")
for f in matriz:
    print(f)

# Para calcular la determinante de la matriz
determinante = np.linalg.det(matriz)
print("Determinante:", round(determinante,1))

