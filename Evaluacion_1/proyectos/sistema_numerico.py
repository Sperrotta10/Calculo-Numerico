# diccionarios para hacer las respectivas conversiones a hexadecimal cuando lo requieran
hexa = {10 : "a",
        11 : "b",
        12 : "c",
        13 : "d",
        14 : "e",
        15 : "f",}

hexa2 = {"a" : 10,
         "b" : 11,
         "c" : 12,
         "d" : 13,
         "e" : 14,
         "f" : 15}


# metodo para indentificar la base
def tipo_base(tipo):

    if(tipo.lower() == "binario"):
        tipo = 2
    elif(tipo.lower() == "octal"):
        tipo = 8
    elif(tipo.lower() == "hexadecimal"):
        tipo = 16
    elif(tipo.lower() == "decimal"):
        tipo = 10
    elif(tipo.lower() == "terciario"):
        tipo = 3
    elif(tipo.lower() == "cuaternario"):
        tipo = 4

    return tipo

# metodo para identificar el tipo de variable
def tipo_variable(tipo,numero):

    if(tipo.lower() == "binario"):
        numero = int(numero)
    elif(tipo.lower() == "octal"):
        numero = int(numero)
    elif(tipo.lower() == "hexadecimal"):
        numero = numero
    elif(tipo.lower() == "decimal"):
        numero = int(numero)
    elif(tipo.lower() == "terciario"):
        numero = int(numero)
    elif(tipo.lower() == "cuaternario"):
        numero = int(numero)

    return numero


# metodo para pasar de decimal a (octal,binario,hexadecimal,ect)
def decimal_cualquier_sistema(numero,tipo,cociente):

    conversion = ""

    if(not(numero < tipo)):
        # el ciclo se va a parar siempre y cuando cociente sea menor a tipo
        while cociente >= tipo:

            cociente = numero // tipo
            residuo = numero % tipo

            # identificamos si el residuo es mayor a 9 para indentificar cuando se hexadecimal y convertir el numero en una letra
            if(residuo > 9):
                residuo = hexa[residuo]

            conversion = str(residuo) + conversion
            numero = cociente

            if(cociente < tipo):

                # identificamos si el cociente es mayor a 9 para indentificar cuando se hexadecimal y convertir el numero en una letra
                if(cociente > 9):
                    cociente = hexa[cociente]
                    
                conversion = str(cociente) + conversion
    else:

        if(tipo == 16 and numero > 9):
            numero = hexa[numero]
        conversion = numero

    return conversion


# metodo para pasa de (octal,binario,hexadecimal, ect) a decimal
def cualquier_sistema_decimal(numero,tipo):

    # num x base^expo
    lista_numero = list(str(numero)) # convertimos el numero en una lista para separarlo por carcteres
    exponente = len(lista_numero) - 1
    conversion = 0
    
    for i in lista_numero:

        # esto es para verificar si hay alguna letra para identificar cuando sea hexadecimal y convertir la letra en numero
        for valor in hexa2:
            if(valor == i):
                i = hexa2[valor]

        conversion += int(i) * (tipo**exponente)
        exponente -= 1

    return conversion


def ejecucion_programa(tipo,numero,cociente,tipo1):

    resultado = 0

    if(tipo == tipo1):
        resultado = numero
    else:

        if(tipo1 == 10):

            resultado = cualquier_sistema_decimal(numero,tipo)
        else:
            numero = cualquier_sistema_decimal(numero,tipo)
            resultado = decimal_cualquier_sistema(numero,tipo1,numero)


    return resultado


#tipo,numero,tipo1 = menu_opcines()
#ejecucion_programa(tipo,numero,numero,tipo1)