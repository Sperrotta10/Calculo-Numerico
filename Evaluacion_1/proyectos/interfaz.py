import flet as ft
import sistema_numerico as sn
import matriz as gj
import random

def main(page: ft.Page):

    # informacion sobre la ventana, alto, ancho, posicion x, y
    page.window_height = 600
    page.window_width = 700
    page.window_center()


    # Manejo de entrada de datos por teclado (Conversion de numeros)
    def opcion_seleccionada(e):

        if(lista1.value == "Binario"):

            entrada.value = ""
            entrada.read_only = False
            entrada.input_filter.regex_string = r"[0-1]"
            
        elif(lista1.value == "Octal"):

            entrada.value = ""
            entrada.read_only = False
            entrada.input_filter.regex_string = r"[0-7]"
            
        elif(lista1.value == "Hexadecimal"):

            entrada.value = ""
            entrada.read_only = False
            entrada.input_filter.regex_string = r"[0-9abcdef]"

        elif(lista1.value == "Decimal"):

            entrada.value = ""
            entrada.input_filter.regex_string = r"[0-9]"
            entrada.read_only = False
            
        elif(lista1.value == "Terciario"):

            entrada.value = ""
            entrada.read_only = False
            entrada.input_filter.regex_string = r"[0-2]"

        elif(lista1.value == "Cuaternario"):

            entrada.value = ""
            entrada.read_only = False
            entrada.input_filter.regex_string = r"[0-3]"

        page.update()


    # layauts de la primera ventana (conversion de numeros)
    entrada = ft.TextField(hint_text="escribe un numero", width=300, bgcolor= "#FFFFFF", border_radius = 10, read_only=True,
                           input_filter=ft.InputFilter(allow=True, regex_string = r"[0-9]", replacement_string=""))
    salida = ft.TextField(width=300, bgcolor= "#FFFFFF", border_radius = 10, read_only=True)

    lista1 = ft.Dropdown(
                    width=135,
                    bgcolor= "#FFFFFF",
                    on_change= opcion_seleccionada,
                    options=[
                        ft.dropdown.Option("Binario"),
                        ft.dropdown.Option("Octal"),
                        ft.dropdown.Option("Hexadecimal"),
                        ft.dropdown.Option("Decimal"),
                        ft.dropdown.Option("Terciario"),
                        ft.dropdown.Option("Cuaternario"),
                    ],
                )
    
    lista2 = ft.Dropdown(
                    width=135,
                    bgcolor= "#FFFFFF",
                    options=[
                        ft.dropdown.Option("Binario"),
                        ft.dropdown.Option("Octal"),
                        ft.dropdown.Option("Hexadecimal"),
                        ft.dropdown.Option("Decimal"),
                        ft.dropdown.Option("Terciario"),
                        ft.dropdown.Option("Cuaternario"),
                    ],
                )
    

    # layauts de la segunda ventana (Gauss-Jordan)
    txt_size = ft.TextField(text_align=ft.TextAlign.RIGHT, width=100, height = 45, bgcolor= "#FFFFFF", 
                            input_filter=ft.InputFilter(allow=True, regex_string = r"[0-9]", replacement_string=""))
    resultado_matriz = ft.TextField(value="", width=260, height = 35, read_only=True, bgcolor= "#FFFFFF")
    matrix_container = ft.Column([])
    matriz_valores = []


    """======================================================= Ventana Principal (Conversion de numeros) ========================================================"""
    # metodo para convertir numeros
    def boton_ejecutar(e):
        
        # si se cumple la condicion de que los campo de texto no esten vacio se ejecuta el programa de lo contrario no pasa nada
        if(lista1.value != None and entrada.value != "" and lista2.value != None):

            # obtenemos los valores donde:
            tipo = sn.tipo_base(lista1.value)                           # tipo es el sistema base del numero que queremos convertir
            numero = sn.tipo_variable(lista1.value,entrada.value)       # numero es el numero que vamos a cconvertir
            cociente = numero                                           # tipo1 es al sistema base que deseamos hacer la conversion
            tipo1 = sn.tipo_base(lista2.value)                          # el cociente es igual al numero

            # metodo que resuelve la conversion
            salida.value = sn.ejecucion_programa(tipo,numero,cociente,tipo1)
            
            page.update()
        else:
            pass
        

    def boton_borrar(e):

        entrada.value = ""            # vaciamos el campo de texto
        entrada.read_only = True      # le indicamos que no pueda ingresar datos
        salida.value = ""             # vaciamos el campo de texto
        lista1.value = None           # vaciamos la opcion seleccionada
        lista2.value = None           # vaciamos la opcion seleccionada
        page.update()


    """==========================================================================================================================================================="""
    


    
    """======================================================= Ventana Secundaria (Gauss-Jordan) ================================================================="""

    # generamos los texfields dependiendo del tamano que asigne el usuario
    def generate_matrix(e):

        # validacion para que solamente se puede generar una matriz 2x2 en adelante
        if(txt_size.value != ""):
            if(int(txt_size.value) >= 2 and int(txt_size.value) <= 6):

                txt_size.read_only = True
                tamano = int(txt_size.value)    # obteneos el valor de las filas y columnas
                matrix_container.controls = []  # Limpia los controles existentes

                for i in range(tamano):

                    # usamos una lista por compresion para generar una serie de filas
                    # dentro de la lista por comprension tenemos dos condiciones, una para identificar el texfield para marcar la igualdad y que no se puede ingresar texto
                    row = ft.Row([ft.TextField(input_filter=ft.InputFilter(allow=True, regex_string = r"[0-9{1,3}]", replacement_string=""),
                                bgcolor= "#FFFFFF", width=60, height= 38, text_align = ft.TextAlign.CENTER,
                                value = "=" if (j == tamano) else "", read_only = (j == tamano)) for j in range(tamano + 2)])
                    
                    matrix_container.controls.append(row)

                page.update()
            else:
                pass
        else:
            pass

    # metodo para borrar los campos de texto
    def borrar_segunda_ventana(e):
        txt_size.value = ""                  # vaciamos el campo del tamano de la matriz
        txt_size.read_only = False           # Habilitamos el campo de texto
        resultado_matriz.value = ""          # vaciamos el campo del resultado del sistema de ecuaciones
        resultado_matriz.width = 260         # asignamos el ancho por defecto del campo de texto
        matrix_container.controls = []       # vaciamos el contenedor donde se almacena todos los texfields de la matriz y el termino independiente
        matriz_valores.clear()

        page.update()

    def validacion_campos_vacios(matrix_container,txt):

        bandera = False
        cont_elementos = 0

        # verificamos si los campos de textos de la matriz y el termino indenpendiente estan vacios
        for fila in matrix_container.controls:
            for texfield in fila.controls:
                if(texfield.value != ""):
                    cont_elementos += 1

        # sabemos que si no se proporciono el tamano de la matriz, mucho menos va a existir la misma, por eso debemos comprobar si el campo esta vacio
        # y si no lo esta ahi verificamos si cada uno de los elementos de la matriz y termino independiente estan rellenados si es asi soltamos un True
        if(txt_size.value != ""):
            if(cont_elementos == (int(txt_size.value) * int(txt_size.value)) + int(txt_size.value) * 2):
                bandera = True

        return bandera


    # metodo con el cual vamos obtener los resultados
    def obtener_valores_matriz(e):

        # esta codicion es para validad que los campos de texto no esten vacios, si lo estan no se ejecuta el metodo
        if(txt_size != "" and validacion_campos_vacios(matrix_container,txt_size)):

            matriz_valores.clear()    # esto es un preventino por si hay valores almacenados los limpiamos
        
            # ciclo para recorrer y obtener los valores de los texfields de la matriz y termino independiente
            for fila in matrix_container.controls:
                fila_valores = []
                for texfield in fila.controls:
                    fila_valores.append(texfield.value)
                matriz_valores.append(fila_valores)

            print(matriz_valores)

            # llamamos el mentodo para resolver el sistema de ecuaciones
            vector_solucion = gj.ejecucion_programa(matriz_valores)
            resultado = ""

            # recorremos el vector con los resultados del sistema para mostralor en una cadena de texto
            for i in range(len(vector_solucion)):
                print(vector_solucion[i])

                if(i == len(vector_solucion) -1):
                    resultado += "r" + str(i+1) + " = " + str(round(vector_solucion[i], 2))
                else:
                    resultado += "r" + str(i+1) + " = " + str(round(vector_solucion[i], 2)) + ", "

            # validacion para cambiar el tamano de la letra dependiendo del numero de incognitas
            if(len(vector_solucion) <= 3):
                resultado_matriz.value = resultado
            elif(len(vector_solucion) <= 5):
                resultado_matriz.text_size = 9
                resultado_matriz.width = 300
                resultado_matriz.value = resultado
            else:
                resultado_matriz.text_size = 9
                resultado_matriz.width = 390
                resultado_matriz.value = resultado

            page.update()
        
        else:
            pass


    # metodo para generar valores aleatorios a la matriz y termino indenpendiente
    def valores_aleatorios(e):
        
        # ciclo para recorrer y obtener los valores de los texfields de la matriz y termino independiente
        for fila in matrix_container.controls:
            for texfield in fila.controls:
                if(texfield.value == ""):
                    texfield.value = random.randint(-10,100)


        page.update()

    """==========================================================================================================================================================="""

    # Definir la vista principal
    def home_view():
        # Crear botones para la navegación
        btn_to_second = ft.ElevatedButton("Gauss-Jordan", on_click=lambda e: page.go("/segunda"))
        
        layout = ft.Column(
            [
            ft.Row([
                btn_to_second,
                ],
                alignment= ft.MainAxisAlignment.CENTER,
            ),
            ft.Row([
                lista1,
                entrada,
                ],
                alignment=ft.MainAxisAlignment.CENTER,
                spacing=40,
            ),
            ft.Row([
                lista2,
                salida,
                ],
                alignment=ft.MainAxisAlignment.CENTER,
                spacing=40,
            ),
            ft.Row([
                ft.ElevatedButton(text = "Ejecutar", width = 205, height = 40, bgcolor= "#4D82BC", color="#FFFFFF", elevation= 5, on_click = boton_ejecutar),
                ft.ElevatedButton(text = "Borrar", width = 205, height = 40, bgcolor= "#4D82BC", color="#FFFFFF", elevation= 5, on_click = boton_borrar),
                ],
                alignment=ft.MainAxisAlignment.CENTER,
                spacing=60,
            )
            
            ],
            expand=True,
            alignment = ft.MainAxisAlignment.CENTER,
            spacing= 50,
            )
        
        page.views.clear()
        page.views.append(ft.View(controls=[layout], bgcolor = "#84B6F4"))
    


    # Definir la segunda vista
    def second_view():
        btn_back_home = ft.ElevatedButton("Conversion de numeros", on_click=lambda e: page.go("/"))

        layout = ft.Column(
            [
            ft.Row([
                btn_back_home,
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            
            ),
            ft.Row([
                txt_size, 
                ft.ElevatedButton("Generar Matriz", height = 40, on_click=generate_matrix, bgcolor= "#4D82BC", color="#FFFFFF", elevation= 5),
                ft.ElevatedButton(text = "Random", width = 135, height = 40, bgcolor= "#4D82BC", color="#FFFFFF", elevation= 5, on_click= valores_aleatorios),
                ],
                alignment=ft.MainAxisAlignment.CENTER,
                spacing= 24.4,
            ),
            ft.Row([
                matrix_container,
            ],
                alignment=ft.MainAxisAlignment.CENTER,
            ),
            ft.Row([
                resultado_matriz,
                ft.ElevatedButton(text = "resultados", width = 140, height = 40, bgcolor= "#4D82BC", color="#FFFFFF", elevation= 5, on_click=obtener_valores_matriz),
            ],
                alignment=ft.MainAxisAlignment.CENTER,
                spacing = 30,
            ),
            ft.Row([
                ft.ElevatedButton(text = "Borrar", width = 300, height = 40, bgcolor= "#4D82BC", color="#FFFFFF", elevation= 5, on_click= borrar_segunda_ventana),
                ],
                alignment=ft.MainAxisAlignment.CENTER,
            ),

        ],
        expand=True,
        alignment = ft.MainAxisAlignment.CENTER,
        spacing= 27
        )

        page.views.clear()
        page.views.append(ft.View(controls= [layout], bgcolor = "#84B6F4"))
    

    

    """======================================================== Controlador del manejo de ventanas ==============================================================="""
    
    # Manejar los cambios de ruta
    def on_route_change(e: ft.RouteChangeEvent):
        if e.route == "/segunda":
            boton_borrar(e)
            second_view()
        else:
            borrar_segunda_ventana(e)
            home_view()
        page.update()
    
    page.on_route_change = on_route_change
    home_view()  # Iniciar con la vista principal
    page.update()


ft.app(target = main)