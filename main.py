import MatrizLibro, MatrizSocios, login, MatrizAdmin, funcionalidades, MatrizPrestamo

# Inicializar la matriz de socios
matrizBibliotecaSocios = MatrizSocios.biblioteca_usuarios

# Mostrar el menú de inicio
login.inicio()

# Solicitar la opción inicial
opcion = int(input("Ingrese su opción: "))
while opcion < 0 or opcion > 3:
    print("Opción inválida. Por favor, elija una opción válida.")
    opcion = int(input("Ingrese su opción: "))

#Bandera es para romper el bucle (terminar el programa)
#Badera_back es para volver atrás en el menú de socio
bandera = True
bandera_back = True
while bandera:
    if opcion == 1:  # Crear cuenta
        while bandera_back:
            nombre_user = input("Ingresar Nombre de Usuario: ")
            contraseña_user = input("Ingresar Contraseña: ")

            # Validar la contraseña
            while not funcionalidades.validContraseña(contraseña_user):
                contraseña_user = input("Ingresar contraseña válida: ")

            funcionalidades.darDeAltaSocio(nombre_user, contraseña_user, matrizBibliotecaSocios)
            bandera, bandera_back = funcionalidades.retroceder_menu()

    elif opcion == 2:  # Iniciar sesión como socio
        if funcionalidades.iniciar_sesion(matrizBibliotecaSocios):
            while bandera_back:
                login.menu_socio()
                variable = int(input("Ingrese su opción: "))
                if variable == 1:  # Submenú de búsqueda de libros
                    login.sub_menuSocio()
                    sub_opcion = int(input("Ingrese su opción: "))
                    if sub_opcion == 1:
                        nombre_autor = input("Ingrese el nombre del autor a buscar: ")
                        funcionalidades.busquedaLibroAutor(MatrizLibro.libros, nombre_autor)
                        bandera, bandera_back = funcionalidades.retroceder_menu()
                    elif sub_opcion == 2:
                        nombre_libro = input("Ingrese el nombre del libro a buscar: ")
                        funcionalidades.busquedaLibroNombre(MatrizLibro.libros, nombre_libro)
                        bandera, bandera_back = funcionalidades.retroceder_menu()
                    elif sub_opcion == 3:
                        id_libro = input("Ingrese el ID del libro a buscar: ")
                        funcionalidades.busquedaLibroID(MatrizLibro.libros, id_libro)
                        bandera, bandera_back = funcionalidades.retroceder_menu()
                        # Modificamos bandera para salir del bucle
                        
                    elif sub_opcion == 0:
                        print("Regresando al menú principal...")
                        break
                    else:
                        print("Opción inválida. Intente nuevamente.")
                elif variable == 2:  # Listar libros
                    print("Mostrando la lista de libros:")
                    funcionalidades.recorrer_matriz(MatrizLibro.libros)
                    bandera, bandera_back = funcionalidades.retroceder_menu()


                elif variable == 3:  # Pedir préstamo
                    nombre_libro = input("Ingrese el nombre del libro que desea pedir prestado: ")


                elif variable == 0:  # Salir del submenú
                    print("Regresando al menú principal...")
                    break
                else:
                    print("Opción inválida. Intente nuevamente.")

    elif opcion == 3:  # Iniciar sesión como administrador
        if funcionalidades.iniciar_sesion(MatrizAdmin.matriz_admin):
            while bandera_back:
                login.menuAdmin()
                opcion_admin = int(input("Ingrese su opción: "))
                if opcion_admin == 1:  # Buscar un libro
                    login.sub_menuSocio()
                    sub_opcion = int(input("Ingrese su opción: "))
                    if sub_opcion == 1:
                        nombre_autor = input("Ingrese el nombre del autor a buscar: ")
                        funcionalidades.busquedaLibroAutor(MatrizLibro.libros, nombre_autor)
                        bandera, bandera_back = funcionalidades.retroceder_menu()
                    elif sub_opcion == 2:
                        nombre_libro = input("Ingrese el nombre del libro a buscar: ")
                        funcionalidades.busquedaLibroNombre(MatrizLibro.libros, nombre_libro)
                        bandera, bandera_back = funcionalidades.retroceder_menu()
                    elif sub_opcion == 3:
                        id_libro = input("Ingrese el ID del libro a buscar: ")
                        funcionalidades.busquedaLibroID(MatrizLibro.libros, id_libro)
                        bandera, bandera_back = funcionalidades.retroceder_menu()
                    elif sub_opcion == 0:
                        print("Regresando al menú principal...")
                        break
                    else:
                        print("Opción inválida. Intente nuevamente.")
                elif opcion_admin == 2:  # Dar de alta un libro
                    nombre_libro = input("Ingrese el nombre del libro: ")
                    if not funcionalidades.chequearLibroRepite(MatrizLibro.libros, nombre_libro):
                        nombre_autor = input("Ingrese el autor del libro: ")
                        MatrizLibro.libros.append([nombre_libro, nombre_autor, len(MatrizLibro.libros) + 1])
                        print("Libro agregado con éxito.")
                        
                    else:
                        print("El libro ya existe en la biblioteca.")
                        bandera, bandera_back = funcionalidades.retroceder_menu()
                elif opcion_admin == 3:  # Dar de baja un libro
                    nombre_libro = input("Ingrese el nombre del libro a dar de baja: ")
                    if funcionalidades.busquedaLibroNombre(MatrizLibro.libros, nombre_libro):
                        MatrizLibro.libros = [libro for libro in MatrizLibro.libros if libro[0] != nombre_libro]
                        print("Libro eliminado con éxito.")
                        bandera, bandera_back = funcionalidades.retroceder_menu()
                    else:
                        print("El libro no se encontró.")
                        bandera, bandera_back = funcionalidades.retroceder_menu()
                elif opcion_admin == 4:  # Modificar un libro
                    nombre_libro = input("Ingrese el nombre del libro a modificar: ")
                    if funcionalidades.busquedaLibroNombre(MatrizLibro.libros, nombre_libro):
                        nuevo_nombre = input("Ingrese el nuevo nombre del libro: ")
                        nuevo_autor = input("Ingrese el nuevo autor del libro: ")
                        for libro in MatrizLibro.libros:
                            if libro[0] == nombre_libro:
                                libro[0] = nuevo_nombre
                                libro[1] = nuevo_autor
                                print("Libro modificado con éxito.")
                                break
                        bandera, bandera_back = funcionalidades.retroceder_menu()
                    else:
                        print("El libro no se encontró.")
                        bandera, bandera_back = funcionalidades.retroceder_menu()
                elif opcion_admin == 5:  # Listar libros
                    print("Mostrando la lista de libros:")
                    funcionalidades.recorrer_matriz(MatrizLibro.libros)
                    bandera, bandera_back = funcionalidades.retroceder_menu()
                elif opcion_admin == 6:  # Dar de alta un socio
                    nombre_user = input("Ingresar Nombre de Usuario: ")
                    contraseña_user = input("Ingresar Contraseña: ")
                    while not login.validContraseña(contraseña_user):
                        contraseña_user = input("Ingresar contraseña válida: ")
                    funcionalidades.darDeAltaSocio(nombre_user, contraseña_user, matrizBibliotecaSocios)
                    print("✅ Cuenta creada con éxito:")
                    print(f"Usuario: {nombre_user} | Email: {nombre_user + '@biblio.edu.ar'}")
                    bandera, bandera_back = funcionalidades.retroceder_menu()
                elif opcion_admin == 7:  # Dar de baja un socio
                    legajo = int(input("Ingrese el número de legajo del socio a eliminar: "))
                    matrizBibliotecaSocios = [socio for socio in matrizBibliotecaSocios if socio[1] != legajo]
                    print("Socio eliminado con éxito.")
                    bandera, bandera_back = funcionalidades.retroceder_menu()
                elif opcion_admin == 8:  # Ver listado de préstamos
                    funcionalidades.recorrer_matriz(MatrizPrestamo.listado_prestamos)
                    bandera, bandera_back = funcionalidades.retroceder_menu()
                elif opcion_admin == 0:  # Salir del submenú
                    print("Regresando al menú principal...")
                    break
                else:
                    print("Opción inválida. Intente nuevamente.")

    elif opcion == 0:  # Salir del programa
        print("Saliendo del programa...")
        bandera = False
    else:
        print("Opción inválida. Intente nuevamente.")