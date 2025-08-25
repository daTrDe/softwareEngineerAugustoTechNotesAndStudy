#This script prompts the user for their name and age, then prints a greeting message.
nombre = input("Ingrese su nombre: ")
print("Hola, " + nombre + "!")
print(type(nombre))  # This will show the type of the variable 'nombre', which is a string.
edad = int(input("Ingrese su edad: "))
print("Tienes ",  edad, " años.")
print(type(edad))  # This will show the type of the variable 'edad', which is an integer. We already converted the input to an integer using int().
