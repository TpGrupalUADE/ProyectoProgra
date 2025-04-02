import MatrizLibro
import MatrizUsuarios
def menu_login():
    print("=" * 30)
    print("¡Bienvenidos a nuestra Biblioteca!".center(30))
    print("Seleccione: ")
    print("1. Crear cuenta")
    print("2. Iniciar sesión")
    print("=" * 30)
def menu():
    print("=" * 30)
    print("Por favor, elija una opción:")
    print("1. Búsqueda de libro")
    print("2. Dar de alta un libro")
    print("3. Dar de baja un libro")
    print("4. Modificar libro")
    print("5. Listar libros")
    print("0. Salir")
    print("=" * 30)
<<<<<<< HEAD
def validContraseña(contraseña_user):
    if len(contraseña_user) < 8:
        return False
    else:
        return True
menu_login()

matrizBibliotecaUsuarios = MatrizUsuarios.biblioteca_usuarios

=======
menu( )
>>>>>>> 33e8d29b77fabc257db5e04a380b4cb1f883b90c
opcion = int(input("Ingrese su opción: "))
while opcion < 0 or opcion > 5:
    print("Opción inválida. Por favor, elija una opción válida.")
    opcion = int(input("Ingrese su opción: "))
while opcion != 0 :
    if opcion == 1:
        nombre_user = input("Ingresar Nombre de Usuario: ")
        #Contraseña debe tener mínimo 8 caracteres; 1 mayus; 1 nro; 1 caracter especial.
        contraseña_user = input("Ingresar Contraseña: ")
        while validContraseña(contraseña_user) != True:
            contraseña_user = input("Ingresar contraseña válida: ")
            validContraseña(contraseña_user)
        matrizBibliotecaUsuarios.append([nombre_user,matrizBibliotecaUsuarios[-1][1]+1,nombre_user + "@biblio.edu.ar",contraseña_user]) 
#    print(matrizBibliotecaUsuarios[-1])
"""
    elif opcion == 2:
        nombre_user = 
        if opcion == 1:
        print("=" * 30)
        print("1. Buscar libro por autor")
        print("2. Buscar libro por nombre")
        print("3. Buscar libro por ID")
        print("0. Retroceder")
        print("=" * 30)
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
        else:
            print("Opción inválida. Por favor, elija una opción válida.")
    elif opcion == 2:
        print("=" * 30)
        
        print("=" * 30)
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

