squares = [x**2 for x in range(1,11)]  # This code demonstrates how to create a list of squares using list comprehension.
print("Squares:", squares)

celsius = [0, 10, 20, 30, 40, 50]
fahrenheit = [((9/5) * temp + 32) for temp in celsius]  # This code demonstrates how to convert Celsius to Fahrenheit using list comprehension.
print("Temperatura en grados Fahrenheit:", fahrenheit)

evens = [x for x in range(1, 21) if x % 2 == 0]  # This code demonstrates how to create a list of even numbers using list comprehension.
print("Números pares del 1 al 20:", evens)