usuarios = [
    [0,120805,"mail1@biblio.edu.ar"],
    [0,120806,"mail2@biblio.edu.ar"],
    [0,120807,"mail3@biblio.edu.ar"],
    [0,120808,"mail4@biblio.edu.ar"],
    [0,120809,"mail5@biblio.edu.ar"]
]
#El max_len calcula los espacios entre dato y otro para obtener la misma separación.
max_len = max(len(str(num)) for fila in usuarios for num in fila)

#Mostrar la matriz usuarios
for fila in usuarios:
    for elemento in fila:
        # Formatear cada elemento con el tamaño adecuado
        print(f"{elemento:{max_len}}", end=" ")                     
    print()  # Salto de línea después de cada fila