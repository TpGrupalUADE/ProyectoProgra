import MatrizLibro
import MatrizUsuarios

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
    print("0. Salir")
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
            break
    if not tiene_mayuscula:
        return 1

    # Verificar si tiene al menos un carácter especial
    caracteres_especiales = "!@#$%^&*()-_=+[]{}|;:'\",.<>?/\\"  # Lista de caracteres especiales permitidos
    tiene_caracter_especial = False
    for char in contraseña_user:
        if char in caracteres_especiales:
            tiene_caracter_especial = True
            break
    if not tiene_caracter_especial:
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

# Importa la matriz de usuarios y la almacena en una variable
matrizBibliotecaUsuarios = MatrizUsuarios.biblioteca_usuarios
# Importa la matriz de libros y la almacena en una variable
matrizLibros = MatrizLibro.libros

# Muestra el menú de inicio de sesión
menu_login()

opcion = int(input("Ingrese su opción: "))
while opcion != 0:
    if opcion == 1:  # Crear cuenta
        while True:
            nombre_user = input("Ingresar Nombre de Usuario o '0' para salir: ")
            if nombre_user == "0":
                print("Saliendo del programa...")
                exit()

            # Verificar si el usuario ya existe
            if usuario_existe(nombre_user, matrizBibliotecaUsuarios):
                print("El usuario ya existe. Intente con otro nombre.")
            else:
                print("Usuario disponible.")
                break

        # Contraseña debe tener mínimo 8 caracteres; 1 mayúscula; 1 carácter especial.
        while True:
            contraseña_user = input("Ingresar Contraseña o '0' para salir: ")
            if contraseña_user == "0":
                print("Saliendo del programa...")
                exit()

            validacion = validContraseña(contraseña_user)
            if validacion == 0:
                print("La contraseña debe tener al menos 8 caracteres.")
            elif validacion == 1:
                print("La contraseña debe tener al menos una letra mayúscula.")
            elif validacion == 2:
                print("La contraseña debe tener al menos un carácter especial.")
            else:
                break  # Contraseña válida, salir del bucle

        # Agregar el usuario a la matriz
        nuevo_id = matrizBibliotecaUsuarios[-1][1] + 1
        matrizBibliotecaUsuarios.append([nombre_user, nuevo_id, nombre_user + "@biblio.edu.ar", contraseña_user])
        print("Usuario agregado exitosamente.")

    elif opcion == 2:  # Iniciar sesión
        nombre_user = input("Ingresar Nombre de Usuario: ")
        contraseña_user = input("Ingresar Contraseña: ")

        # Verificar si el usuario existe y si la contraseña es correcta
        usuario_encontrado = False
        for fila in matrizBibliotecaUsuarios:
            if fila[0] == nombre_user and fila[3] == contraseña_user:
                usuario_encontrado = True
                print(f"Hola {nombre_user}, un gusto verte de nuevo!")
                menu()
                opcion = int(input("Ingrese su opción: "))
                if opcion == 1:
                    menu_Busqueda()
                    sub_opcion = int(input("Ingrese su opción: "))
                    if sub_opcion == 1:
                        print("Buscando libro por autor...")
                    elif sub_opcion == 2:
                        print("Buscando libro por nombre...")
                    elif sub_opcion == 3:
                        print("Buscando libro por ID...")
                    elif sub_opcion == 0:
                        print("Regresando al menú principal...")
                    else:
                        print("Opción inválida. Por favor, elija una opción válida.")
                elif opcion == 2:
                    print("Dar de alta un libro...")
                elif opcion == 3:
                    print("Dar de baja un libro...")
                elif opcion == 4:
                    print("Modificar libro...")
                elif opcion == 5:
                    print("Listando libros...")
                    max_len = max(len(str(num)) for fila in matrizLibros for num in fila)
                    for fila in matrizLibros:
                        for elemento in fila:
                            print(f"{elemento:{max_len}}", end=" ")
                        print()
                elif opcion == 0:
                    print("Saliendo del programa...")
                    exit()
                else:
                    print("Opción inválida. Por favor, elija una opción válida.")
                break

        if not usuario_encontrado:
            print("Nombre de usuario o contraseña incorrectos.")

    else:
        print("Opción inválida. Por favor, elija una opción válida.")

    opcion = int(input("\nPara salir presione '0': "))

print("Saliendo del programa...")