import flet as ft
import sistema_numerico as sn

def main(page: ft.Page):

    # informacion sobre la ventana, alto, ancho, posicion x, y
    page.window_height = 500
    page.window_width = 700
    page.window_left = 330
    page.window_top = 135


    # layauts de la primera ventana (conversion de numeros)
    entrada = ft.TextField(hint_text="escribe un numero", width=300, bgcolor= "#FFFFFF", border_radius = 10)
    salida = ft.TextField(width=300, bgcolor= "#FFFFFF", border_radius = 10, read_only=True)
    lista1 = ft.Dropdown(
                    width=135,
                    bgcolor= "#FFFFFF",
                    options=[
                        ft.dropdown.Option("Binario"),
                        ft.dropdown.Option("Octal"),
                        ft.dropdown.Option("Hexadecimal"),
                        ft.dropdown.Option("Decimal"),
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
                    ],
                )


    # metodo para convertir numeros
    def boton_ejecutar(e):
        
        # si se cumple la condicion de que los campo de texto no esten vacio se ejecuta el programa de lo contrario no pasa nada
        if(lista1.value != None and entrada.value != None and lista2.value != None):

            # obtenemos los valores donde:
            
            tipo = sn.tipo_base(lista1.value)                           # tipo es el sistema base del numero que queremos convertir
            numero = sn.tipo_variable(lista1.value,entrada.value)       # numero es el numero que vamos a cconvertir
            cociente = numero                                           # tipo1 es al sistema base que deseamos hacer la conversion
            tipo1 = sn.tipo_base(lista2.value)                          # el cociente es igual al numero
            
            print(str(tipo) + " " + str(numero) + " " + str(cociente) + " " + str(tipo1))

            # metodo que resuelve la conversion
            salida.value = sn.ejecucion_programa(tipo,numero,cociente,tipo1)
            
            page.update()
        else:
            pass
        

    def boton_borrar(e):

        salida.value = ""
        page.update()

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
            
            ],expand=True,
            alignment = ft.MainAxisAlignment.SPACE_EVENLY,
            #spacing= 20,
            )
        
        page.views.clear()
        #page.views.append(ft.View(controls=[btn_to_second, ft.TextField(hint_text="escribir")]))
        page.views.append(ft.View(controls=[layout], bgcolor = "#84B6F4"))
    

    # Definir la segunda vista
    def second_view():
        btn_back_home = ft.ElevatedButton("Conversion de numeros", on_click=lambda e: page.go("/"))
        page.views.clear()
        page.views.append(ft.View(controls= [btn_back_home]))
    

    # Manejar los cambios de ruta
    def on_route_change(e: ft.RouteChangeEvent):
        if e.route == "/segunda":
            second_view()
        else:
            home_view()
        page.update()
    
    page.on_route_change = on_route_change
    home_view()  # Iniciar con la vista principal
    page.update()


ft.app(target = main)