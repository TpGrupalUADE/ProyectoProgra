#Archivo para agregar funciones que realicen algo en específico

def busquedaLibroAutor(matriz, nombre_autor):
    print(f"Buscando libros del autor: {nombre_autor}")
    libros_encontrados = []
    for libro in matriz:
        if libro[1].lower() == nombre_autor.lower():  # Comparar ignorando mayúsculas/minúsculas
            libros_encontrados.append(libro)
    if libros_encontrados:
        print("Libros encontrados:")
        for libro in libros_encontrados:
            print(f"- {libro[0]} (ID: {libro[2]})")  # Mostrar nombre del libro y su ID
    else:
        print("No se encontraron libros de ese autor.")

def busquedaLibroNombre(matriz, nombre_libro):
    print(f"Buscando libro: {nombre_libro}")
    libros_encontrados = []
    for libro in matriz:
        if libro[0].lower() == nombre_libro.lower():  # Comparar ignorando mayúsculas/minúsculas
            libros_encontrados.append(libro)
    if libros_encontrados:
        print("Libros encontrados:")
        for libro in libros_encontrados:
            print(f"- {libro[0]} (ID: {libro[2]})")  # Mostrar nombre del libro y su ID
    else:
        print("No se encontraron libros con ese nombre.")

def busquedaLibroID(matriz, id_libro):
    print(f"Buscando libro con ID: {id_libro}")
    libros_encontrados = []
    for libro in matriz:
        if libro[2] == id_libro:  # Comparar el ID directamente
            libros_encontrados.append(libro)
    if libros_encontrados:
        print("Libros encontrados:")
        for libro in libros_encontrados:
            print(f"- {libro[0]} (Autor: {libro[1]}, ID: {libro[2]})")  # Mostrar nombre, autor e ID del libro
    else:
        print("No se encontraron libros con ese ID.")

def chequearLibroRepite(matriz, libro):
    for i in range(len(matriz)):
        if matriz[i][0] == libro:
            print("El libro ya existe en la biblioteca.")
            return True
    return False

def darDeAltaSocio (nombre_usuario, contrasena, matriz_usuario):
    nuevo_id = matriz_usuario[-1][1] + 1                                #Le asigna a "nuevo_id" el ID del último usuario + 1
    nuevo_email = nombre_usuario + "@biblio.edu.ar"

    matriz_usuario.append([nombre_usuario, nuevo_id, nuevo_email, contrasena]) #Agrega el nuevo usuario a la matriz de usuarios
    print("✅ Cuenta creada con éxito:")
    print(f"Usuario: {nombre_usuario} | Email: {nombre_usuario+ '@biblio.edu.ar'}") #Muestra el usuario y el email del nuevo usuario creado

#def darDeBajaSocio(id, matriz_usuario):


def validContraseña(contraseña_user):
    tiene_mayuscula = False
    tiene_numero = False
    tiene_especial = False

    especiales = "!@#$%^&*(),.?\":{}|<>_-+="

    errores = []

    if len(contraseña_user) < 8:
        errores.append("Debe tener al menos 8 caracteres.")

    for caracter in contraseña_user:        #Recorre cada caracter de la contraseña, chequeando que tenga cada característica solicitada
        if caracter.isupper():              #Chequea si tiene mayúscula
            tiene_mayuscula = True
        if caracter.isdigit():              #Chequea si tiene número
            tiene_numero = True
        if caracter in especiales:          #Chequea si tiene carácter especial
            tiene_especial = True

    if not tiene_mayuscula:                 #En caso de no tener alguna de las características, se agrega a la lista de errores
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