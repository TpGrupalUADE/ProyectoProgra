    #Este es el programa con funciones LOGIN 
def inicio():
    print("=" * 30)
    print("¡Bienvenidos a nuestra Biblioteca!".center(30))
    print("Seleccione: ")
    print("1. Crear cuenta")
    print("2. Iniciar sesión como socio")
    print("3. Iniciar sesión como administrador")
    print("=" * 30)

def menu_socio():
    print("=" * 30)
    print("Por favor, elija una opción:")
    print("1. Búsqueda de libro")
    print("2. Listar libros")
    print("0. Salir")
    print("=" * 30)

def iniciar_sesion(matriz):
    nombre = input("Nombre de usuario: ")
    contraseña = input("Contraseña: ")

    encontrado = False
    for usuario in matriz:
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


def menuAdmin():
    print("=" * 30)
    print("1. Búsqueda de libro")
    print("2. Dar de alta un libro")
    print("3. Dar de baja un libro")
    print("4. Modificar libro")
    print("5. Listar libros")
    print("6. Dar de alta un socio")
    print("7. Dar de baja un socio")
    print("0. Salir")
    print("=" * 30)

def sub_menuSocio():
    print("=" * 30)
    print("1. Buscar libro por autor")
    print("2. Buscar libro por nombre")
    print("3. Buscar libro por ID")
    print("0. Salir")
    print("=" * 30)

