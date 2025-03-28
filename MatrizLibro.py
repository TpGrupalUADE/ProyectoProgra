#FILAS DE LIBROS (NOMBRE / AUTOR / ID):
inventario_libro = [
    ["IT", "Sthepen King", "001"],
    ["El exorcista", "William Peter Blatty", "002"],
    ["Drácula", "Bram Stoker", "003"],
    ["El resplandor", "Stephen King", "004"],
    ["Frankenstein", "Mary Shelley", "005"],
    ["El silencio de los corderos", "Thomas Harris", "305"],
    ["Orgullo y prejuicio", "Jane Austen", "101"],
    ["Bajo la Misma Estrella", "John Green", "102"],
    ["Cumbres borrascosas", "Emily Brontë", "103"],
    ["Posdata: Te amo", "Cecelia Ahern", "104"],
    ["Un paseo para recordar", "Nicholas Sparks", "105"],
    ["Los juegos del hambre", "Suzanne Collins", "201"],
    ["La isla del tesoro", "Robert Louis Stevenson", "202"],
    ["El Código Da Vinci", "Dan Brown", "203"],
    ["Jurassic Park", "Michael Crichton", "204"],
    ["Misión Imposible", "Bruce Geller", "205"],
    ["Asesinato en el Orient Express", "Agatha Christie", "301"],
    ["El Sabueso de los Baskerville", "Arthur Conan Doyle", "302"],
    ["La chica del tren", "Paula Hawkins", "303"],
    ["Los hombres que no amaban a las mujeres", "Stieg Larsson", "304"],
    ["El Señor de los Anillos", "J.R.R. Tolkien", "401"],
    ["Harry Potter y la piedra filosofal", "J.K. Rowling", "402"],
    ["Crónica del asesino de reyes (El nombre del viento)", "Patrick Rothfuss", "403"],
    ["Juego de tronos", "George R.R. Martin", "404"],
    ["Alicia en el país de las maravillas", "Lewis Carroll", "405"]
]

# Calcular el ancho máximo de cada columna
ancho_columna = [max(len(str(fila[i])) for fila in inventario_libro) for i in range(len(inventario_libro[0]))]
""" 
# Imprimir la matriz con formato
print("Matriz de Libros:")
print("=" * (sum(ancho_columna) + len(ancho_columna) * 3 - 1))  # Línea separadora
for fila in inventario_libro:
    for i, elemento in enumerate(fila):
        # Formatear cada elemento con el ancho de columna adecuado
        print(f"{str(elemento):<{ancho_columna[i]}}", end=" | ")
    print()  # Salto de línea después de cada fila
print("=" * (sum(ancho_columna) + len(ancho_columna) * 3 - 1))  # Línea separadora
"""