# Creación y escritura en el archivo my_notes.txt
with open('my_notes.txt', 'w') as file:
    # Escribimos tres líneas de notas personales actualizadas
    file.write("Nota 1: Organizar el horario de estudio para la semana.\n")
    file.write("Nota 2: Investigar sobre nuevas librerías de Python.\n")
    file.write("Nota 3: Realizar un resumen del capítulo 4 del libro de algoritmos.\n")

# Lectura del archivo my_notes.txt línea por línea
with open('my_notes.txt', 'r') as file:
    # Leemos y mostramos cada línea del archivo
    line = file.readline()
    while line:
        print(line.strip())  # strip() elimina el salto de línea al final
        line = file.readline()
