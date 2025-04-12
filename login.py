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
    print("3. Pedir préstamo")
    print("0. Salir")
    print("=" * 30)

def menuAdmin():
    print("=" * 30)
    print("1. Búsqueda de libro")
    print("2. Dar de alta un libro")
    print("3. Dar de baja un libro")
    print("4. Modificar libro")
    print("5. Listar libros")
    print("6. Dar de alta un socio")
    print("7. Dar de baja un socio")
    print("8. Ver listado préstamo")
    print("0. Salir")
    print("=" * 30)

def sub_menuSocio():
    print("=" * 30)
    print("1. Buscar libro por autor")
    print("2. Buscar libro por nombre")
    print("3. Buscar libro por ID")
    print("0. Salir")
    print("=" * 30)