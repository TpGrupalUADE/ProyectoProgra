biblioteca_usuarios = [
    ["Juana", 120805, "mail1@biblio.edu.ar", "contrasena1"],
    ["Pedro", 120806, "mail2@biblio.edu.ar", "contrasena2"],
    ["Tomas", 120807, "mail3@biblio.edu.ar", "contrasena3"],
    ["Lucas", 120808, "mail4@biblio.edu.ar", "contrasena4"],
    ["Santi", 120809, "mail5@biblio.edu.ar", "contrasena5"],
]
#FORMATO MATRIZ -> [Nombre, ID, Correo, Contraseña] -> [0, 1, 2, 3]

# Calcular el ancho máximo de cada columna
ancho_columna = [max(len(str(fila[i])) for fila in biblioteca_usuarios) for i in range(len(biblioteca_usuarios[0]))]

# Imprimir la matriz con formato
"""for fila in biblioteca_usuarios:
print("Matriz de Usuarios:")
print("=" * (sum(ancho_columna) + len(ancho_columna) * 3 - 1))  # Línea separadora
    for i, elemento in enumerate(fila):
        # Formatear cada elemento con el ancho de columna adecuado
        print(f"{str(elemento):<{ancho_columna[i]}}", end=" | ")
    print()  # Salto de línea después de cada fila
print("=" * (sum(ancho_columna) + len(ancho_columna) * 3 - 1))  # Línea separadora"""
print("Matriz de Usuarios:", biblioteca_usuarios)