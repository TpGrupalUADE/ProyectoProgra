import MatrizLibro
import MatrizSocios
import login
import MatrizAdmin

matrizBibliotecaSocios = MatrizSocios.biblioteca_usuarios

login.menu_login()

opcionLogin = int(input("Ingrese su opción: "))
while opcionLogin < 0 or opcionLogin > 5:
    print("Opción inválida. Por favor, elija una opción válida.")
    opcionLogin = int(input("Ingrese su opción: "))

while opcionLogin != 0:
    if opcionLogin == 1:
        nombre_user = input("Ingresar Nombre de Usuario: ")
        
        contraseña_user = input("Ingresar Contraseña: ")
        while not login.validContraseña(contraseña_user):
            contraseña_user = input("Ingresar contraseña válida: ")

        nuevo_id = matrizBibliotecaSocios[-1][1] + 1
        nuevo_email = nombre_user + "@biblio.edu.ar"

        matrizBibliotecaSocios.append([nombre_user, nuevo_id, nuevo_email, contraseña_user])
        print("✅ Cuenta creada con éxito:")
        print(f"Usuario: {nombre_user} | Email: {nuevo_email}")

    elif opcionLogin == 2:
        if login.iniciar_sesion(matrizBibliotecaSocios):

#Cerrar bucle de inicio de sesion!!!
            login.menu()
            opcion = int(input("Ingrese opcion: "))
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
                else:
                    print("Opción inválida. Por favor, elija una opción válida.")
            elif opcion == 2:
                print(MatrizLibro.libros)
            else:
                break

    elif opcion == 3:
        login.iniciar_sesion(MatrizAdmin)

        login.menuAdmin()

    opcionLogin=0

    """elif opcion == 2:
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
    opcion = int(input("\nIngrese otra opción o 0 para salir: "))"""

    