import numpy as np



"""
Este es mi algoritmo de Gauss Jordan hecho por mi, tiene un pequeño detalle y es solamente 
cuando se encuentra algun 0 en la diagonal principal, cuando se encuentra un cero (pivote)
directamente no hace la operacion porque tengo una condicion para que no caiga en condicion de
error, ya que no se puede dividir entre cero, en el resto de los casos funciona bien 
"""



class GaussJordan:
    def __init__(self,matriz,vector):
        self.matriz = matriz
        self.vector = vector

    def resolver_sistema_ecuaciones(self):

        # evitar error de truncamiento
        self.matriz = np.array(self.matriz, dtype=float)

        AB = np.concatenate((self.matriz,self.vector), axis = 1)

        # Matriz aumentada
        fila_columnas = np.shape(AB)

        # tamano de las filas y columnas
        fila = fila_columnas[0]
        columnas = fila_columnas[1]


        # colocar ceros en la triangular inferior
        for i in range(fila - 1):

            for j in range(0,fila-i-1,1):
                if(AB[i,i] != 0):
                    f = AB[i,:]/AB[i,i]
                    AB[j+i+1,:] = AB[j+i+1,:] - AB[j+i+1,i] * f


        # colocar ceros a la triangular superior
        for i in range(fila-1):

            for j in range(fila-(fila-1)+i):
                if(AB[i+1,i+1] != 0):
                    f = AB[i+1,:]/AB[i+1,i+1]
                    AB[j,:] = AB[j,:] - AB[j,i+1] * f


        # convertir todo los pivotes a 1
        for i in range(fila):
            AB[i,:] = AB[i,:]/AB[i,i]


        x = AB[:,columnas - 1]
        print(AB)

        return x


def transformar_matrizNp(matriz_valores, matriz, vector):

    for f in range(len(matriz_valores)):
        filas_matriz = []
        filas_vector = []
        for c in range(len(matriz_valores[0])):

            # condicion para que cundo c igual "=" no lo tome en cuenta y otras dos para separar la matriz de los terminos independientes
            if(c == len(matriz_valores[0]) - 2):
                pass
            elif(c == len(matriz_valores[0]) - 1):
                filas_vector.append(int(matriz_valores[f][c]))
            else:
                filas_matriz.append(int(matriz_valores[f][c]))
        matriz.append(filas_matriz)
        vector.append(filas_vector)


def ejecucion_programa(matriz_valores):

    # deifinimos dos listas vacias
    matriz = []
    vector = []
    #matriz_valores = [[1,2,"=",3],[4,5,"=",6]]

    # metodo para recorrer la matriz de valores y separar la matriz, de los terminos independientes
    transformar_matrizNp(matriz_valores, matriz, vector)

    # convertimos a arrays de numpy
    a = np.array(matriz)
    b = np.array(vector)

    # creamos un objeto y resolvemos el sistema de ecuaciones
    gaussJordan1 = GaussJordan(a,b)
    resultado = gaussJordan1.resolver_sistema_ecuaciones()
    return resultado

#ejecucion_programa()