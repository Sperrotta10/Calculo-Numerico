# Operaciones Aritmeticas Basicas

# Suma
230 + 120

# Resta
1450 - 1223

# Multiplicacion
12 * 10

# Division
10 / 2

# Division Entera
28 %/% 3

# Division Residual
20 %% 7

# Jerarquia de Operaciones

# primero lo que esta dentro del parentesis
# segundo la multiplicacion
# tercero la division
# luego la suma y la resta

# Operadores Logicos

# AND
TRUE & TRUE
TRUE & FALSE
FALSE & FALSE

# OR
TRUE | TRUE
TRUE | FALSE
FALSE | TRUE
FALSE | FALSE



# Variables

x <- 100
y <- "Hola, Mundo"
z <- z2 <- TRUE

assign("a",1450) # Una de las formas para asignar variables
a

# verificar si una variable ya existe
exists("a")
exists("f")

# Elminar una Variables
rm("a")

# ls() lo que hace es crear una lista con todas las variables que tenemos
# rm(list = ls()) lo que hace es borrar todas las variables



# Tipos de Datos
class(x) # --> Numeric
class(y) # --> character
class(z) # --> Logical

# Factor
fac <- factor("Santiago")
fac

# Date
fecha <- as.Date("2020-09-28")
fecha


# Estructura de Datos

# Vectores
vec <- c(1,2,3,4)
vec

# DataFrames
tabla <- data.frame(x = 1:10, y = 11:20)
tabla

# Listas
lista = list(x = tabla, y = vec)
lista
