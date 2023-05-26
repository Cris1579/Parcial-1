# Crear dos matrices donde la cantidad de filas y columnas serán 3 x 3. Los
# elementos de estas matrices deben ser generados de forma aleatoria (-5 a -10).
# Luego se deben multiplicar ambas matrices e imprimir la matriz resultante.
# Agregar una condición para que las dimensiones sean acordes para realizar la
# multiplicación entre ambas matrices.
# Esta matriz resultado se debe multiplicar por una matriz identidad, e imprimir la matriz final.
import random
filas = 3
columnas = 3
def Crear_matrizz(filas,columnas):
    m = []
    for i in range(filas):
        fila = []
        for j in range(columnas):
            elemt = random.randint(-10,-5)
            fila.append(elemt)
        m.append(fila)
    return m

def Mult_matriz(M1,M2):
    matriz_final = []
    for i in range(len(M1)):
        fila = []
        for j in range(len(M2[0])):
            mult = M1[i][j] * M2 [i][j]
            fila.append(mult)
        matriz_final.append(fila)
    return matriz_final


M1 = Crear_matrizz(3,3)
print("La primera matriz generada es: ")
for x in M1:
    print(x)

M2 = Crear_matrizz(3,3)
print("\nLa segunda matriz generada es: ")
for y in M2:
    print(y)
M3 = Mult_matriz(M1,M2)
print("\nLa multiplicación entre ambas matrices es: ")
for z in M3:
    print(z)

MtxIdn= [
    [1,0,0],
    [0,1,0],
    [0,0,1],
]

if len(M3) == len(MtxIdn):
    def Mult_matrizIden(M3,MtxIdn):
        mf = []
        for i in range(len(M3)):
            fila = []
            for j in range(len(MtxIdn[0])):
                mult = M3[i][j] * MtxIdn [i][j]
                fila.append(mult)
            mf.append(fila)
        return mf
else:
    print("Las dimensiones son distintas, no se pueden multiplicar")

M4 = Mult_matrizIden(M3,MtxIdn)
print("\nLa multiplicación con la matriz Identidad es: ")
for W in M4:
    print(W)
