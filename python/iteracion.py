numbers = [1, 2, 3, 4, 5]
for i in numbers:
    print("Aquí i es igual a:", i+1) # This code demonstrates how to iterate over a list using a for loop.

for i in range(3,10):
    print("Aquí i es igual a:", i) 

fruits = ["manzana", "banana", "cereza", "Carambolota ca"]
for fruta in fruits:
    print("Fruta:", fruta)
    if fruta == "banana":
        print("Encontré una banana")

x = 0
while x< 5:
    if x==3:
        print("x es igual a 3, saliendo del bucle")
        break
    print("x es igual a:", x) 
    x +=1

numbers = [1, 2, 3, 4, 5]
for i in numbers:
    if i == 3:
        continue
    print("Aquí i es igual a:", i+1) # This code demonstrates how to iterate and use of continue.