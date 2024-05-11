conversion = ""

hexa = {10 : "a",
        11 : "b",
        12 : "c",
        13 : "d",
        14 : "e",
        15 : "f"}

numero = int(input("Escoja el numero decimal que desee: "))
cociente = numero
print("1- Binario \n2- Octal \n3-Hexadecimal")
tipo = int(input("Que conversion desearia realizar: "))

if(tipo == 1):
    tipo = 2
elif(tipo == 2):
    tipo = 8
elif(tipo == 3):
    tipo = 16




def decimal_cualquier_sistema(numero,tipo,cociente):

    conversion = ""

    while cociente >= tipo:

        cociente = numero // tipo
        residuo = numero % tipo

        if(residuo > 9):
            residuo = hexa[residuo]

        conversion = str(residuo) + conversion
        numero = cociente

        if(cociente < tipo):

            if(cociente > 9):
                cociente = hexa[cociente]
                
            conversion = str(cociente) + conversion

    return conversion


def cualquier_sistema_decimal(numero,tipo):

    lista_numero = list(numero)
    print(lista_numero)


print(cualquier_sistema_decimal(numero,0))
#print(decimal_cualquier_sistema(numero,tipo,cociente))