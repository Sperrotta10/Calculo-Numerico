import numpy as np

class GaussJordan:
    def __init__(self,matriz,vector):
        self.matriz = matriz
        self.vector = vector

    def resolver_sistema_ecuaciones(self):

        # evitar error de truncamiento
        self.matriz = np.array(self.matriz, dtype=float)

        AB = np.concatenate((self.matriz,self.vector), axis = 1)

        # Pivoteo parcial por filas
        tamano = np.shape(AB)
        n = tamano[0]
        m = tamano[1]

        # Para cada fila en AB
        for i in range(0,n-1,1):
            # columna desde diagonal i en adelante
            columna = abs(AB[i:,i])
            dondemax = np.argmax(columna)
            
            # dondemax no está en diagonal
            if (dondemax !=0):
                # intercambia filas
                temporal = np.copy(AB[i,:])
                AB[i,:] = AB[dondemax+i,:]
                AB[dondemax+i,:] = temporal
                

        # eliminacion hacia adelante
        for i in range(0,n-1,1):
            pivote = AB[i,i]
            adelante = i + 1
            for k in range(adelante,n,1):
                factor = AB[k,i]/pivote
                AB[k,:] = AB[k,:] - AB[i,:]*factor


        # elimina hacia atras
        ultfila = n-1
        ultcolumna = m-1
        for i in range(ultfila,0-1,-1):
            pivote = AB[i,i]
            atras = i-1 
            for k in range(atras,0-1,-1):
                factor = AB[k,i]/pivote
                AB[k,:] = AB[k,:] - AB[i,:]*factor
            # diagonal a unos
            AB[i,:] = AB[i,:]/AB[i,i]
        x = np.copy(AB[:,ultcolumna])

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