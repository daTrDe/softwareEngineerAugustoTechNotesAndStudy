x = 5
if x > 5:
    print("x es mayor que 5")
elif x == 5:
    print("x es igual a 5") #Podemos poner varios elif
else:
    print("x no es mayor que 5")
print("Aquí estamos afuera del bloque if")

x = 15
y = 20
if x>10 and y>25:
    print("x es mayor que 10 y y es mayor que 25")

    if x>10 or y>25:
        print("x es mayor que 10 o y es mayor que 25")

if not x>10:
    print("x no es mayor que 10")


is_member = True
edad = 15

if is_member:
    if edad>=15:
        print("Puedes entrar al club")
    else:
        print("No puedes entrar al club, debes ser mayor de 15 años")
else:
    print("Debes ser miembro del club para entrar")