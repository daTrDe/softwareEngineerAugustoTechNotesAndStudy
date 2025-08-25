# This code demonstrates the use of matrices and tuples in Python.
# This code prints a matrix and a list of tuples, demonstrating how to work with these data structures in Python.
matrix = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]
print("Matrix:")
print(matrix)
print(matrix[0])
for row in matrix:
    print(row)
#The matrix is mutable, meaning you can change its elements.

numbers = (1, 2, 3, 4, 5) #Si le quito los parentesis, python lo intepreta como una tupla también.
print("\nTuples:")
for t in numbers:
    print(t)
numbers[0] = "unos"
#The tuples are immutable, meaning you cannot change their elements.