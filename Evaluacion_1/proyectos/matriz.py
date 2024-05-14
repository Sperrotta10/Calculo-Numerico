import numpy as np

class GaussJordan:
    def __init__(self,matriz,vector):
        self.matriz = matriz
        self.vector = vector

    def resolver_sistema_ecuaciones(self):
        tamano = len(self.vector)

        # evitar error de truncamiento
        self.matriz = np.array(self.matriz, dtype=float)

        AB = np.concatenate((self.matriz,self.vector), axis = 1)

        for i in range(tamano):
            maximo_i = np.argmax(abs(AB[i:, i])) + i
            AB[[i, maximo_i]] = AB[[maximo_i, i]]
            pivote = AB[i, maximo_i]
            AB[i] = AB[i] / pivote

            for j in range(tamano):
                if(i != j):
                    AB[j] = AB[j] - AB[j,i] * AB[i]

        x = AB[:, -1]
        return x


def transformar_matrizNp(matriz_valores, matriz, vector):

    filas_vector = []
    for f in range(len(matriz_valores)):
        filas_matriz = []
        for c in range(len(matriz_valores[0])):

            # condicion para que cundo c igual "=" no lo tome en cuenta y otras dos para separar la matriz de los terminos independientes
            if(c == len(matriz_valores[0]) - 2):
                pass
            elif(c == len(matriz_valores[0]) - 1):
                filas_vector.append(matriz_valores[f][c])
            else:
                filas_matriz.append(matriz_valores[f][c])
        matriz.append(filas_matriz)
    vector.append(filas_vector)


def ejecucion_programa():

    # deifinimos dos listas vacias
    matriz = []
    vector = []
    matriz_valores = [[1,2,"=",3],[4,5,"=",6]]

    # metodo para recorrer la matriz de valores y separar la matriz, de los terminos independientes
    transformar_matrizNp(matriz_valores, matriz, vector)

    # convertimos a arrays de numpy
    a = np.array(matriz)
    b = np.array(vector)

    # creamos un objeto
    gaussJordan1 = GaussJordan(a,b)
    resultado = gaussJordan1.resolver_sistema_ecuaciones()
    print(resultado)

ejecucion_programa()