"""
EJERCICIO PRACTICO: POO
fecha: 16 de abril 2024
seccion: 305C1 
Estudiante: Santiago Perrotta

Actividad
1. Crear una clase PERSONA
2. Atributos de la clase: nombre,edad,identificacion
3. Metodos: constructor, sets,gets, mostrar datos,
Devolver mediante un valor logico si es mayor de edad
4. validar datos en la consola

caso 1: datos ingresados por el teclado
caso 2: matriz generada
caso 3: determinar cuantos mayores de edad hay
"""

class Persona:
    
    # Metodo constructor vacio
    def __init__(self):
        self.nombre = ""
        self.edad = 0
        self.dni = ""

    # Metodos getters para los atributos de la clase

    def getterNombre(self):
        return self.nombre
    
    def getterEdad(self):
        return self.edad
    
    def getterDni(self):
        return self.dni
    
    # Metodos setter para los atributos de la clase

    def setterNombre(self,nombre):
        self.nombre = nombre
    
    def setterEdad(self,edad):
        self.edad = edad
    
    def setterDni(self,dni):
        self.dni = dni

    # funcion para mostrar los atributos de la clase
    def mostrarDatos(self):
        print("Nombre: " + self.nombre)
        print("edad: " + str(self.edad))
        print("cedula: " + self.dni)

    # funcion para indicar true si la persona es mayor de edad
    def mayorEdad(self):
        if(self.edad >= 18):
            return True
        else:
            return False
        

# funciones para la entrada de datos por teclado y validacion de datos

def validacionNombre():

    while True:
        nombre = input("Escriba su nombre: ")

        # el ciclo se va a romper cuando solamente sean caracteres
        if(nombre.isalpha()):
            break
        else:
            print("\nError, escriba caracteres\n")

    return nombre


def validacionEdad():

    while True:
        
        band = False

        # esta excepcion es para capturar que sea solamente un numero y si es asi activa la bandera a true
        try:
            edad = int(input("Escriba su edad: "))
            band = True
        except ValueError:
            print("\nError, ingrese una edad valida\n")

        # cuando la bandera sea true va a aplicar la siguiente condicion, que es que sea mayor a cero y menor 100 para poder salir del ciclo
        if(band):
            if(edad > 0 and edad < 100):
                break
            else:
                print("\nError, escriba una edad mayor a cero\n")

    return edad
    

def validacionCedula():

    while True:

        dni = input("Escriba su cedula: ")

        # verifica si no son caracteres y ademas que tenga un tamaño entre 6 y 8 digitos
        if(not (dni.isalpha()) and (len(dni) > 5 and len(dni) < 9)):
            break
        else:
            print("\nError, escriba una cedula valida\n")

    return dni

print("\nPrimera Parte del Ejerccio:\n")

nombre = validacionNombre()
edad = validacionEdad()
dni = validacionCedula()

persona1 = Persona()
persona1.setterNombre(nombre)
persona1.setterEdad(edad)
persona1.setterDni(dni)

print("")

persona1.mostrarDatos()
print("Es mayor de edad? --> " + str(persona1.mayorEdad()))

print("\nSeguna Parte del ejercicio")

filas = int(input("Indique la cantidad de personas que desea registrar: "))

# matriz con el registro de las personas
personas = []


# bucle para generar la matriz de los registros de las personas
for f in range(filas):
    registro = []

    # entrada de datos por teclado
    nombre = validacionNombre()
    registro.append(nombre)
    edad = validacionEdad()
    registro.append(edad)
    dni = validacionCedula()
    registro.append(dni)

    # agregamos este registro a la lista de personas
    personas.append(registro)

# blucle para crear los objetos segun la cantidad de registros
objetos = []

for i in range(len(personas)):
    persona = Persona()
    persona.setterNombre(personas[i][0])
    persona.setterEdad(personas[i][1])
    persona.setterDni(personas[i][2])
    objetos.append(persona)

# ahora verificamos cuantas personas mayor de edad hay

print("")
contMayoresEdad = 0
for i in range(len(objetos)):
    if(objetos[i].mayorEdad()):
        contMayoresEdad += 1

print("Hay " + str(contMayoresEdad) + " personas mayores de edad")