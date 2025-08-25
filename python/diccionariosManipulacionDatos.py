# Aquí puedes ver ejemplos de cómo usar y manipular datos en Python. Valores y claves.
numbers ={1:"uno", 2:"dos", 3:"tres"}
print(numbers[2])
information = {"Nombre": "David",
               "Apellido": "Trujillo",
               "Edad": 30,
               "Altura": 1.75,}
print(information)
# Acceder a un valor específico en el diccionario
del information["Edad"]  # Eliminar la clave "Edad"
print(information) # Imprimir el diccionario después de eliminar la clave "Edad"

claves = information.keys()  # Obtener las claves del diccionario
print("Claves del diccionario:", claves)  # Imprimir las claves del diccionario
print(type(claves))  # Imprimir el tipo de las claves, que es un objeto dict_keys
valores = information.values()  # Obtener los valores del diccionario
print("Valores del diccionario:", valores)  # Imprimir los valores del diccionario

pares = information.items()  # Obtener los pares clave-valor del diccionario
print("Pares clave-valor del diccionario:", pares)  # Imprimir los pares clave-valor del diccionario, separados por comas
# Escribiendo David y Ana como claves y sus datos como valores en un diccionario. Comparando con SQL esto sería poner David y Ana como filas y sus datos como columnas.
contactos = {"David": {"Apellido": "Trujillo",
               "Edad": 30,
               "Altura": 1.75,},
               "Ana": {"Apellido": "Gómez",
               "Edad": 28,
               "Altura": 1.65,}}
print(contactos)  # Imprimir el diccionario de contactos
print(contactos["David"])  # Imprimir los datos de David
print(contactos["Ana"]["Edad"])  # Imprimir la edad de Ana