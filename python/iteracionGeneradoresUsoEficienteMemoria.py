#Creamos una lista
my_lista = [1, 2, 3, 4]

#Obtener el iterador
my_iter = iter(my_lista)

#Usar el iterador para recorrer la lista
print(next(my_iter))  # Imprime el primer elemento: 1   La funcion next() obtiene el siguiente elemento del iterador.
print(next(my_iter))  # Imprime el segundo elemento: 2
print(next(my_iter))  # Imprime el tercer elemento: 3
print(next(my_iter))  # Imprime el cuarto elemento: 4
## print(next(my_iter))  # Intentar obtener el siguiente elemento causará un error StopIteration


text = "Hola mundo"
my_iter_text = iter(text) # Usar el iterador para recorrer el texto
for char in my_iter_text:
    print(char)  # Imprime cada carácter del texto "Hola mundo"


#Crear un iterador para los numeros impares
limit = 10

odd_itter = iter(range  (1, limit + 1, 2))  # range(start, stop, step) genera números impares desde 1 hasta limit (exclusivo)
for num in odd_itter:
    print(num)  # Imprime los números impares: 1, 3, 5, 7, 9

def my_generator():
    yield 1
    yield 2
    yield 3

for value in my_generator():
    print(value)  # Imprime los valores generados: 1, 2, 3

#Fibonacci generator 0 1 1 2 3 5 8 13 21 34...
def fibonacci(limit):
    a, b = 0, 1
    while a < limit:
        yield a
        a, b = b, a + b
for num in fibonacci(10):
    print(num)  # Imprime los números de Fibonacci menores que 10: 0, 1, 1, 2, 3, 5, 8
