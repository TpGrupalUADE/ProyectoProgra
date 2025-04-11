import MatrizLibro, MatrizSocios, login, MatrizAdmin, funcionalidades

matrizBibliotecaSocios = MatrizSocios.biblioteca_usuarios

login.inicio()

opcion = int(input("Ingrese su opción: "))
while opcion < 0 or opcion > 3:
    print("Opción inválida. Por favor, elija una opción válida.")
    opcion = int(input("Ingrese su opción: "))

bandera = True
while bandera:
    if opcion == 1:
        nombre_user = input("Ingresar Nombre de Usuario: ")
        
        contraseña_user = input("Ingresar Contraseña: ")
        while not funcionalidades.validContraseña(contraseña_user):
            contraseña_user = input("Ingresar contraseña válida: ")

        funcionalidades.darDeAltaSocio(nombre_user, contraseña_user, matrizBibliotecaSocios)

        #ACA HAY UN BUG PORQUE NUNCA SE ROMPE EL WHILE HASTA QUE PONGA BANDERA = FALSE
        #ENTONCES UNA VEZ TERMINADA LA CREACIÓN DE LA CUENTA, SE PREGUNTA SI QUIERE HACER ALGO MÁS
        #PERO NO HAY OPCIÓN PARA HACER ALGO MÁS, SOLO SE PUEDE SALIR DEL PROGRAMA

    elif opcion == 2:
        if funcionalidades.iniciar_sesion(matrizBibliotecaSocios):

            login.menu_socio()
            variable = int(input("Ingrese su opción: "))


            if variable == 1:
                
                login.sub_menuSocio()
                sub_opcion = int(input("Ingrese su opción: "))

                #bandera = False para salir del programa después de hacer la búsqueda

                if sub_opcion == 1:
                    nombre_autor = input("Ingrese el nombre del autor a buscar: ")
                    #Llamo a la función de búsqueda por autor
                    funcionalidades.busquedaLibroAutor(MatrizLibro.libros, nombre_autor)
                    bandera = False
                elif sub_opcion == 2:
                    nombre_libro = input("Ingrese el nombre del libro a buscar: ")
                    #Llamo a la función de búsqueda por nombre
                    funcionalidades.busquedaLibroNombre(MatrizLibro.libros, nombre_libro)
                    bandera = False
                elif sub_opcion == 3:
                    id_libro = input("Ingrese el ID del libro a buscar: ")
                    #Llamo a la función de búsqueda por ID
                    funcionalidades.busquedaLibroID(MatrizLibro.libros, id_libro)
                    bandera = False


            elif variable == 2:
                print(MatrizLibro.libros)
                bandera = False
            elif variable == 0:
                bandera = False

    elif opcion == 3:
        if login.iniciar_sesion(MatrizAdmin.matriz_admin):
            login.menuAdmin()
            #Ingreso opción para el sub menú del ADMINISTRADOR (no importa que se repita la variable opción)
            opcion = int(input("Ingrese su opción: "))

            if opcion == 1:

                #Buscar un libro

                login.sub_menuSocio()
                sub_opcion = int(input("Ingrese su opción: "))

                #bandera = False para salir del programa después de hacer la búsqueda

                if sub_opcion == 1:
                    nombre_autor = input("Ingrese el nombre del autor a buscar: ")
                    #Llamo a la función de búsqueda por autor
                    funcionalidades.busquedaLibroAutor(MatrizLibro.libros, nombre_autor)
                    bandera = False
                elif sub_opcion == 2:
                    nombre_libro = input("Ingrese el nombre del libro a buscar: ")
                    #Llamo a la función de búsqueda por nombre
                    funcionalidades.busquedaLibroNombre(MatrizLibro.libros, nombre_libro)
                    bandera = False
                elif sub_opcion == 3:
                    id_libro = input("Ingrese el ID del libro a buscar: ")
                    #Llamo a la función de búsqueda por ID
                    funcionalidades.busquedaLibroID(MatrizLibro.libros, id_libro)
                    bandera = False

            elif opcion == 2:
                
                #Dar de alta un libro

                nombre_libro = input("Ingrese el nombre del libro: ")
                #Si el libro no existe en la matriz, no se puede agregar
                if funcionalidades.chequearLibroRepite(MatrizLibro.libros, nombre_libro) == False:
                    nombre_autor = input("Ingrese el autor del libro: ")
                    MatrizLibro.libros.append([nombre_libro, nombre_autor, len(MatrizLibro.libros) + 1])
                else:
                    print("El libro ya existe en la biblioteca.")

            elif opcion == 3:

                #Dar de baja un libro
                #Usar .remove() o .pop() para eliminar el libro de la matriz
                #Dar de baja por nombre del libro
                nombre_libro = input("Ingrese nombre del libro a dar de baja: ")

            elif opcion == 4:

                #Modificar un libro
                #Preguntar nombre del libro a modificar

                nombre_libro = input("Ingrese nombre del libro a modificar")

            elif opcion == 5:

                #Listar libros

                print(MatrizLibro.libros)
            
            elif opcion == 6:

                #Dar de alta un socio
                nombre_user = input("Ingresar Nombre de Usuario: ")
                contraseña_user = input("Ingresar Contraseña: ")

                while not login.validContraseña(contraseña_user):
                    contraseña_user = input("Ingresar contraseña válida: ")

                funcionalidades.darDeAltaSocio(nombre_user, contraseña_user, matrizBibliotecaSocios)

                print("✅ Cuenta creada con éxito:")
                print(f"Usuario: {nombre_user} | Email: {nombre_user+ "@biblio.edu.ar"}")

            elif opcion == 7:

                #Dar de baja un socio
                #Preguntar numero de legajo para eliminar de matriz
                legajo = int(input("Ingrese el número de legajo del socio a eliminar: "))

            elif opcion == 0:
                bandera = False