# Crear el diccionario inicial con información ficticia
informacion_personal = {
    "nombre": "Ana López",
    "edad": 28,
    "ciudad": "Madrid",
    "profesion": "Diseñadora gráfica"
}

# Acceder y modificar el valor de "ciudad"
ciudad_actual = informacion_personal["ciudad"]
print(f"Ciudad original: {ciudad_actual}")
informacion_personal["ciudad"] = "Barcelona"
print(f"Ciudad modificada: {informacion_personal['ciudad']}")

# Agregar una nueva clave-valor para "profesion" (aunque ya existe, la actualizamos o agregamos si no)
# En este caso, como ya existe, la modificamos para simular la adición de nueva información
informacion_personal["profesion"] = "Desarrolladora de software"  # Nueva profesión ficticia

# Verificar existencia de la clave "telefono" y agregarla si no existe
if "telefono" not in informacion_personal:
    informacion_personal["telefono"] = "+34 600 123 456"  # Número ficticio
    print("Clave 'telefono' agregada.")
else:
    print("La clave 'telefono' ya existe.")

# Eliminar la clave "edad"
if "edad" in informacion_personal:
    del informacion_personal["edad"]
    print("Clave 'edad' eliminada.")

# Imprimir el diccionario final
print("\nDiccionario final:")
print(informacion_personal)
