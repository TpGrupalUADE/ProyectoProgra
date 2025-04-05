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

def validContraseña(contraseña_user):
    tiene_mayuscula = False
    tiene_numero = False
    tiene_especial = False

    especiales = "!@#$%^&*(),.?\":{}|<>_-+="

    errores = []

    if len(contraseña_user) < 8:
        errores.append("Debe tener al menos 8 caracteres.")

    for caracter in contraseña_user:
        if caracter.isupper():
            tiene_mayuscula = True
        if caracter.isdigit():
            tiene_numero = True
        if caracter in especiales:
            tiene_especial = True

    if not tiene_mayuscula:
        errores.append("Debe contener al menos una letra mayúscula.")
    if not tiene_numero:
        errores.append("Debe contener al menos un número.")
    if not tiene_especial:
        errores.append("Debe contener al menos un carácter especial.")

    if errores:
        print("Contraseña inválida:")
        for error in errores:
            print(f"- {error}")
        return False

    return True

def iniciar_sesion(matrizUsuarios):
    nombre = input("Nombre de usuario: ")
    contraseña = input("Contraseña: ")

    encontrado = False
    for usuario in matrizUsuarios:
        if usuario[0] == nombre:
            encontrado = True
            if usuario[3] == contraseña:
                print(f"✅ ¡Bienvenido/a {nombre}!")
                return True
            else:
                print("❌ Contraseña incorrecta.")
                return False
    if not encontrado:
        print("❌ Usuario no encontrado.")
    return False


matrizBibliotecaUsuarios = MatrizUsuarios.biblioteca_usuarios

menu_login()

opcion = int(input("Ingrese su opción: "))
while opcion < 0 or opcion > 5:
    print("Opción inválida. Por favor, elija una opción válida.")
    opcion = int(input("Ingrese su opción: "))

while opcion != 0:
    if opcion == 1:
        nombre_user = input("Ingresar Nombre de Usuario: ")
        
        contraseña_user = input("Ingresar Contraseña: ")
        while not validContraseña(contraseña_user):
            contraseña_user = input("Ingresar contraseña válida: ")

        nuevo_id = matrizBibliotecaUsuarios[-1][1] + 1
        nuevo_email = nombre_user + "@biblio.edu.ar"

        matrizBibliotecaUsuarios.append([nombre_user, nuevo_id, nuevo_email, contraseña_user])
        print("✅ Cuenta creada con éxito:")
        print(f"Usuario: {nombre_user} | Email: {nuevo_email}")

    elif opcion == 2:
        iniciar_sesion(matrizBibliotecaUsuarios)

#Cerrar bucle de inicio de sesion!!!

        #nombre_user = 
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
    opcion = int(input("\nIngrese otra opción o 0 para salir: "))

    