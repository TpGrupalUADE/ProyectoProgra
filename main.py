import MatrizLibro
import MatrizUsuarios

def menu():
    print("=" * 30)
    print("¡Bienvenidos a nuestra Biblioteca!".center(30))
    print("=" * 30)
    print("Por favor, elija una opción:")
    print("1. Búsqueda de libro")
    print("2. Dar de alta un libro")
    print("3. Dar de baja un libro")
    print("4. Modificar libro")
    print("5. Listar libros")
    print("0. Salir")
    print("=" * 30)
menu( )
opcion = int(input("Ingrese su opción: "))
while opcion < 0 or opcion > 5:
    print("Opción inválida. Por favor, elija una opción válida.")
    opcion = int(input("Ingrese su opción: "))

while opcion != 0:
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
    elif opcion in [2, 3, 4, 5]:
        print(f"Has seleccionado la opción {opcion}.")
        # Agregar la lógica para las opciones 2, 3, 4 y 5
    else:
        print("Opción inválida. Por favor, elija una opción válida.")

    opcion = int(input("Ingrese su opción: "))
    while opcion < 0 or opcion > 5:
        print("Opción inválida. Por favor, elija una opción válida.")
        opcion = int(input("Ingrese su opción: "))