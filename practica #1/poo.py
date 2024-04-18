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
        

# entrada de datos por teclado
nombre = input("Escriba su nombre: ")
edad = int(input("Escriba su edad: "))
dni = input("Escriba su cedula: ")

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
    nombre = input("\nEscriba su nombre: ")
    registro.append(nombre)
    edad = int(input("Escriba su edad: "))
    registro.append(edad)
    dni = input("Escriba su cedula: ")
    registro.append(dni)

    # agregamos este registro a lam lista de personas
    personas.append(registro)

# blucle para crear los objetos segun la cantidad de registros
objetos = []

for i in range(len(personas)):
    persona = Persona()
    persona.setterNombre(personas[i][0])
    persona.setterEdad(personas[i][1])
    persona.setterDni(personas[i][2])
    objetos.append(persona)

# ahora verificamos en el registro cual de las personas es mayor de edad

print("")
for i in range(len(objetos)):
    if(objetos[i].mayorEdad()):
        objetos[i].mostrarDatos()
        print("Es mayor de edad\n")



