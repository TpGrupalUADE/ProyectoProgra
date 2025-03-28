biblioteca_usuarios = [
    [0, 120805, "mail1@biblio.edu.ar"],
    [0, 120806, "mail2@biblio.edu.ar"],
    [0, 120807, "mail3@biblio.edu.ar"],
    [0, 120808, "mail4@biblio.edu.ar"],
    [0, 120809, "mail5@biblio.edu.ar"]
]

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