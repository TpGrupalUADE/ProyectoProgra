import MatrizUsuarios
import MatrizLibro
def menu_Busqueda():
    print("=" * 30)
    print("1. Buscar libro por autor")
    print("2. Buscar libro por nombre")
    print("3. Buscar libro por ID")
    print("0. Retroceder")
    print("=" * 30)

def menu_login():
    # Menú de inicio de sesión
    print("=" * 30)
    print("¡Bienvenidos a nuestra Biblioteca!".center(30))
    print("Seleccione: ")
    print("1. Crear cuenta")
    print("2. Iniciar sesión")
    print("=" * 30)

def menu():
    # Menú de opciones
    print("=" * 30)
    print("1. Búsqueda de libro")
    print("2. Dar de alta un libro")
    print("3. Dar de baja un libro")
    print("4. Modificar libro")
    print("5. Listar libros")
    print("0. Salir")
    print("=" * 30)

def usuario_existe(nombre_user, matriz):
    # Verifica si el usuario ya existe en la matriz
    for fila in matriz:
        if fila[0] == nombre_user:  # Compara con el primer elemento de cada fila (nombre de usuario)
            return True
    return False
    
def validContraseña(contraseña_user):
    # Verificar si tiene al menos 8 caracteres
    if len(contraseña_user) < 8:
        return 0

    # Verificar si tiene al menos una letra mayúscula
    tiene_mayuscula = False
    for letra in contraseña_user:
        if letra.isupper():
            tiene_mayuscula = True
            break  # Salir del bucle si se encuentra una mayúscula
    if not tiene_mayuscula:
        return 1

    # Verificar si tiene al menos un carácter especial
    caracteres_especiales = "!@#$%^&*()-_=+[]{}|;:'\",.<>?/\\"
    if not any(char in caracteres_especiales for char in contraseña_user):
        return 2

    # Si pasa todas las verificaciones, es válida
    return True

def sub_menuLibros():
    print("=" * 30)
    print("1. Buscar libro por autor")
    print("2. Buscar libro por nombre")
    print("3. Buscar libro por ID")
    print("0. Retroceder")
    print("=" * 30)

# Muestra el menú de inicio de sesión
menu_login()

#Importa la matriz de usuarios y la almacena en una variable
matrizBibliotecaUsuarios = MatrizUsuarios.biblioteca_usuarios
#Importa la matriz de libros y la almacena en una variable
matrizLibros = MatrizLibro.libros

opcion = int(input("Ingrese su opción: "))
while opcion != 0:

    #Si el usuario elige "Crear cuenta", se le pide que ingrese un nombre de usuario y una contraseña.
    if opcion == 1:
        while True:
            nombre_user = input("Ingresar Nombre de Usuario o '0' para salir: ")
            if nombre_user == "0":
                print("Saliendo del programa...")
                exit()  # Finaliza el programa

            # Verificar si el usuario ya existe caso contrario se agrega a la matriz
            while usuario_existe(nombre_user, matrizBibliotecaUsuarios):
                print("El usuario ya existe. Intente con otro nombre.")
                nombre_user = input("Ingresar Nombre de Usuario o '0' para salir: ")
            else:
                print("Usuario disponible.")

        # Contraseña debe tener mínimo 8 caracteres; 1 mayúscula; 1 número; 1 carácter especial.
        while True:
            contraseña_user = input("Ingresar Contraseña o '0' para salir: ")
            while contraseña_user == "0":
                print("Saliendo del programa...")
                exit()  # Finaliza el programa

            if validContraseña(contraseña_user) == 0:
                print("La contraseña debe tener al menos 8 caracteres.")
                
            elif validContraseña(contraseña_user) == 1:
                print("La contraseña debe tener al menos una letra mayúscula.")
                
            elif validContraseña(contraseña_user) == 2:
                print("La contraseña debe tener al menos un carácter especial.")
                
            else:
                break  # Contraseña válida, salir del bucle
        matrizBibliotecaUsuarios.append([nombre_user,matrizBibliotecaUsuarios[-1][1]+1,nombre_user + "@biblio.edu.ar",contraseña_user])
        print("Usuario agregado exitosamente.")
#    print(matrizBibliotecaUsuarios[-1])

    # Si el usuario elige "Iniciar sesión", se le pide que ingrese su nombre de usuario y contraseña.

    elif opcion == 2:
        nombre_user = input("Ingresar Nombre de Usuario: ")
        contraseña_user = input("Ingresar Contraseña: ")
        # Verificar si el usuario existe y si la contraseña es correcta
        for fila in matrizBibliotecaUsuarios:
            if fila[0] == nombre_user and fila[3] == contraseña_user:
                print("Inicio de sesión exitoso.")
                # Mostrar el menú de opciones después de iniciar sesión
                print(f"Hola {nombre_user}, un gusto verte de nuevo!")
                menu()
                opcion = int(input("Ingrese su opción: "))
                if opcion == 1:
                    menu_Busqueda()
                    sub_opcion = int(input("Ingrese su opción: "))
                    if sub_opcion == 1:
                        print("Buscando libro por autor...")
                        # Agregar la lógica para buscar por autor
                    elif sub_opcion == 2:
                        print("Buscando libro por nombre...")
                        # Agregar la lógica para buscar por nombre
                    elif sub_opcion == 3:
                        print("Buscando libro por ID...")
                        # Agregar la lógica para buscar por ID
                    elif sub_opcion == 0:
                        print("Regresando al menú principal...")
                        menu()
                        opcion = int(input("Ingrese su opción: "))
                    else:
                        print("Opción inválida. Por favor, elija una opción válida.")
            elif opcion == 2:
                print("Dar de alta un libro...")
                # Agregar la lógica para dar de alta un libro
            elif opcion == 3:
                print("Dar de baja un libro...")
                # Agregar la lógica para dar de baja un libro
            elif opcion == 4:
                print("Modificar libro...")
                # Agregar la lógica para modificar un libro
            elif opcion == 5:
                #Listar libros
                # Calcular el ancho máximo de cada columna
                max_len = max(len(str(num)) for fila in matrizLibros for num in fila)
                for fila in matrizLibros:
                    for elemento in fila:
                        # Formatear cada elemento con el tamaño adecuado
                        print(f"{elemento:{max_len}}", end=" ")                     #El max_len calcula los espacios entre dato y otro para obtener la misma separación.
                    print()  # Salto de línea después de cada fila
                break
            elif opcion == 0:
                print("Saliendo del programa...")
                exit()  # Finaliza el programa
            else:
                print("Nombre de usuario o contraseña incorrectos.")


    
    """ 
        
    elif opcion in [2, 3, 4, 5]:
        print(f"Has seleccionado la opción {opcion}.")
        # Agregar la lógica para las opciones 2, 3, 4 y 5
    else:
        print("Opción inválida. Por favor, elija una opción válida.")

    opcion = int(input("Ingrese su opción: "))
    while opcion < 0 or opcion > 5:
        print("Opción inválida. Por favor, elija una opción válida.")
        opcion = int(input("Ingrese su opción: "))

        """

