#Este es un programa de gestión de biblioteca. Se ingresa con usuario y contraseña,
#habiendo tres intentos como límite.
#Se puede ver el listado de los libros existentes,
#buscar un libro por título o por ID, agregar, editar o eliminar una obra.
#Los cambios se guardan en json.


import json
import colorama
colorama.init()



#LISTA DE DICCIONARIOS con descripción de libros
libros_biblioteca = [
    {
        "id": 1,
        "titulo_libro" : "100 años de soledad",
        "nombre_autor" : "Garcia Marquez", 
        "precio_libro" : "10000"
    },
    {
        "id": 2,
        "titulo_libro" : "El tunel",
        "nombre_autor" : "Sabato",
        "precio_libro" : "9500"
    },
    {
        "id": 3,
        "titulo_libro" : "Triste,solitario y final",
        "nombre_autor": "Soriano",
        "precio_libro" : "10500"
    },
    {
        "id": 4,
        "titulo_libro" : "Dinero,credito y bancos",
        "nombre_autor" : "Keynes",
        "precio_libro" : "15000"
    }
]





#FUNCIONES que se utilizarán en el programa principal

def ver_opciones_menu():#Función utilizada en el match para elegir la opción que invocará otras funciones para poder realizarla
    print("\nElija una opción: \n")
    print(colorama.Fore.MAGENTA +"1)"+colorama.Fore.RESET, "Ver listado de libros") #Se utiliza colorama para resaltar los números de opción a elegir
    print(colorama.Fore.MAGENTA +"2)"+colorama.Fore.RESET, "Buscar un libro")
    print(colorama.Fore.MAGENTA +"3)"+colorama.Fore.RESET, "Agregar un nuevo libro")
    print(colorama.Fore.MAGENTA +"4)"+colorama.Fore.RESET, "Editar un libro de la lista")
    print(colorama.Fore.MAGENTA +"5)"+colorama.Fore.RESET, "Eliminar un libro de la lista")
    print(colorama.Fore.MAGENTA +"6)"+colorama.Fore.RESET, "Salir del programa\n")

def ver_listado():#Esta función recorre el listado de los libros de la biblioteca con un for y luego los imprime en formato de tabla
    for i in libros_biblioteca:
        print(f"{i['id']}    {i['titulo_libro'].ljust(30)}{i['nombre_autor'].ljust(30)}${i['precio_libro'].ljust(30)}")

def buscar_libro (criterio):
    # Buscar por ID si el criterio es un número
    if criterio.isdigit():#pregunta por si es un digito
        id_busqueda = int(criterio) #convierto el digito en entero
        for e in libros_biblioteca:
            if e ["id"] == id_busqueda:
                print("Libro encontrado: \n")
                print("∘"*71)
                print (colorama.Fore.CYAN + f"\n{'ID'}   {'TÍTULO'.ljust(30)}{'AUTOR'.ljust(30)}{'PRECIO'.ljust(30)}" + colorama.Fore.RESET )
                print(f"{e ['id']}    {e ['titulo_libro'].ljust(30)}{e ['nombre_autor'].ljust(30)}${e['precio_libro'].ljust(30)}\n")
                #Con .ljust() se está alineando y separando los títulos y descripción de los libros para que quede ordenada la tabla 
                print("∘"*71)
                return
        print(f"Libro con ID {criterio} no encontrado")
    else:
        # Buscar por nombre si el criterio NO es un número
        for e in libros_biblioteca:
            if e["titulo_libro"].lower() == criterio.lower():#Con .lower() igualamos los títulos para poder compararlos correctamente
                print("\nLibro encontrado: \n")
                print("∘"*71)
                print (colorama.Fore.CYAN + f"{'ID'}   {'TÍTULO'.ljust(30)}{'AUTOR'.ljust(30)}{'PRECIO'.ljust(30)}" + colorama.Fore.RESET )
                print(f"{e ['id']}    {e ['titulo_libro'].ljust(30)}{e ['nombre_autor'].ljust(30)}${e['precio_libro'].ljust(30)}")
                print("∘"*71)
                return
        print(f'Libro con el nombre "{criterio}" no encontrado')

def agregar_libros(libro,autor,precio):#Esta función permite agregar un nuevo libro con su descripción, y le asignará un número de ID
    global proximo_id
    
    libro_nuevo = {
        "id":proximo_id,
        "titulo_libro": libro,
        "nombre_autor" : autor,
        "precio_libro" : precio
    }
    
    libros_biblioteca.append(libro_nuevo)#.append() agregará un nuevo libro al final de la lista
    proximo_id += 1


def editar_libro(libro_a_editar):#Se podrá editar el título, autor o precio de los libros
    for x in libros_biblioteca:#Con el for recorrerá la lista de la biblioteca buscando el título ingresado
        if(x["titulo_libro"].lower() == libro_a_editar.lower()):#Se igualan a minúsculas los títulos para comparar
            nuevo_titulo_libro = input(f"Ingrese el nuevo título del libro para reemplazar a {libro_a_editar}: ").title()
            nuevo_nombre_autor = input(f"Ingrese el nuevo nombre del autor para reemplazar a  {libro_a_editar}: ").title() 
            nuevo_precio_libro = input(f"Ingrese el nuevo precio para reemplazar a {libro_a_editar}: ")
            x["titulo_libro"] = nuevo_titulo_libro
            x["nombre_autor"] = nuevo_nombre_autor
            x["precio_libro"] = nuevo_precio_libro
            
            print(colorama.Fore.GREEN +"Descripcion Actualizada con EXITO"+colorama.Fore.RESET)
            return

    print(f"Libro con el nombre {libro_a_editar} no encontrado")#Devuelve este mensaje si no encuentra el título ingresado

def eliminar_libro(libro_a_borrar):#Se buscará un libro por su título luego de igualar a minúsculas, y se procederá a borrarlo con .remove()
    for x in libros_biblioteca:
        if(x["titulo_libro"].lower() == libro_a_borrar.lower()):
            libros_biblioteca.remove(x)
            print  (f"libro: {libro_a_borrar} eliminado con exito") 
            return

    print(f"El libro {libro_a_borrar} no se ha encontrado")#Devuelve este mensaje si no encuentra el título ingresado

def verificar_credenciales(user,password):#En esta función se compara usuario y contraseña ingresada con las guardadas en las listas. Devolverá True o False
    for i in range(len(listado_usuarios)):
        if(listado_usuarios[i] == user and listado_pass[i] == password):
            return True
        
    return False

def limitar_texto(nuevo_titulo_libro, max_caracteres):#Función para limitar un título extenso y que entre con prolijidad en la tabla de la lista de libros
    if len(nuevo_titulo_libro) > max_caracteres:
        return nuevo_titulo_libro[:max_caracteres - 3] + "..."
    return nuevo_titulo_libro


def guardar_en_json():#Permite guardar los cambios que se hayan realizado para reutilizarlos
    with open(archivo_json, 'w') as archivo:
        json.dump(libros_biblioteca, archivo, indent=4)


def cargar_de_json():
    global libros_biblioteca, proximo_id
    try:
        with open(archivo_json, 'r') as archivo:
            libros_biblioteca = json.load(archivo)
            if libros_biblioteca:
                proximo_id = max(libro["id"] for libro in libros_biblioteca) + 1
    except FileNotFoundError:
        guardar_en_json()  


#----ESTRUCTURA PRINCIPAL DEL PROGRAMA-----

#Variables y listas
acceso_concedido = False    
listado_usuarios = ["marcos","luciano","maga","jime", "miche"]
listado_pass = ["123","456", "789", "000" , "159"]
intentos = 3
correr_biblioteca = True
proximo_id = 5
archivo_json = 'biblioteca.json'

cargar_de_json() #Se carga desde el archivo json los cambios guardados


while (correr_biblioteca == True): #Mientras el bloque while sea True correrá infinitamente
        if(acceso_concedido == False): #El acceso concedido es False hasta que se ingresa el usuario y contraseña correctos
    
            usuario_nuevo = input(  colorama.Fore.YELLOW + "\nIngrese  Usuario: "  + colorama.Fore.RESET)
            password_nuevo = input(  colorama.Fore.YELLOW + "Ingrese  Contraseña: " + colorama.Fore.RESET)

            
            print("\n•⋅⊰∙∘ ───⋆｡°✩⋅•⋅⊰∙∘☽༓☾∘∙⊱⋅•⋅✩°｡⋆─── ∘∙⊱⋅•⋅\n")
            if(verificar_credenciales(usuario_nuevo,password_nuevo) == True):
                print(colorama.Fore.GREEN + "BIENVENIDO a la BIBLIOTECA MAGIC".center(42) + colorama.Fore.RESET)
                print("\n•⋅⊰∙∘ ───⋆｡°✩⋅•⋅⊰∙∘☽༓☾∘∙⊱⋅•⋅✩°｡⋆─── ∘∙⊱⋅•⋅\n")
                acceso_concedido = True #Si el acceso concedido pasa a ser True se entra al menú del programa
            else:
                intentos= intentos - 1 #De no serlo se comienza a restar los intentos fallidos permitidos con un contador
                if(intentos <= 0 ):
                    print(colorama.Back.RED + "ACCESO DENEGADO" + colorama.Back.RESET)
                    print(colorama.Fore.RED + "Excediste los intentos fallidos." + colorama.Fore.RESET)
                    break
                else:
                    print(f"Te quedan: {colorama.Back.RED} {intentos} {colorama.Back.RESET} intentos restantes. ") #Se comunica los intentos que van quedando   
                
        else:
            ver_opciones_menu() #Aquí se utiliza un match para elegir la opción deseada
            opcion_seleccionada = int(input("Opción elegida: "))
            match opcion_seleccionada:
                case 1:
                    print("\n•⋅⊰∙∘ ──────────────────⋆｡°✩⋅•⋅⊰∙∘☽༓☾∘∙⊱⋅•⋅✩°｡⋆────────────────── ∘∙⊱⋅•⋅\n")
                    print (colorama.Fore.CYAN + f"{'ID'}   {'TÍTULO'.ljust(30)}{'AUTOR'.ljust(30)}{'PRECIO'.ljust(30)}" + colorama.Fore.RESET)
                    ver_listado() #Llamado a la función que nos mostrará el listado
                    print("\n•⋅⊰∙∘ ──────────────────⋆｡°✩⋅•⋅⊰∙∘☽༓☾∘∙⊱⋅•⋅✩°｡⋆────────────────── ∘∙⊱⋅•⋅\n")
                case 2:
                    criterio = input("Ingrese el libro que busca: ")
                    buscar_libro(criterio) #Llamado a la función de búsqueda
                case 3: 
                    nuevo_titulo_libro = input("Ingrese el título del nuevo libro: ").title()
                    texto_limitado = limitar_texto(nuevo_titulo_libro, 25)
                    
                    nuevo_nombre_autor = input("Ingrese el apellido del nuevo autor: ").title()
                    nuevo_precio_libro = input("Ingrese el precio del nuevo libro: ")
                    agregar_libros(texto_limitado,nuevo_nombre_autor,nuevo_precio_libro) #Llamado a la función que agregará el libro
                    guardar_en_json()
                    print(colorama.Fore.GREEN + "Libro agregado con EXITO ! "+ colorama.Fore.RESET)
                case 4:
                    libro_a_editar = input("Ingrese el título del libro a EDITAR: ")
                    editar_libro(libro_a_editar) #Llamado a la función que permite editar el libro
                    guardar_en_json()
                    print(colorama.Fore.GREEN + "Libro editado con  EXITO ! "+ colorama.Fore.RESET)
                case 5:
                    libro_a_borrar = input("Ingrese el nombre del libro que quieras borrar: ")
                    eliminar_libro(libro_a_borrar) #Llamado a la función para eliminar un libro
                    guardar_en_json()
                    print(colorama.Fore.GREEN + "Libro eliminado con EXITO ! "+ colorama.Fore.RESET)
                case 6:
                    print(colorama.Fore.RED +"\n📚 SALIENDO DEL PROGRAMA ¡LO ESPERAMOS NUEVAMENTE! 📚\n"+ colorama.Fore.RESET) #Mensaje de despedida al elegir salir del programa
                    correr_biblioteca = False #La variable se convierte en False, lo que hace que deje de correr
                case _:
                    print (colorama.Fore.RED + "Selecciona una opción valida"+colorama.Fore.RESET) 
                    #Aparecerá este mensaje en caso que el usuario ingrese una opción diferente a las que se mencionan
