#Si quiero copiar solo la infomracion y no apuntar hacia la memory de la lista original, debo usar el slicing.
a = [1, 2, 3, 4, 5]
b = a
print(a)
print(b)
del a [0]
print("Después de eliminar el primer elemento de 'a':")
print("Lista a:", a)
print("Lista b:", b)
#Ambas listas apuntan a la misma referencia en memoria, por lo que al modificar 'a', 'b' también se ve afectada.

# Usando slicing para copiar la lista
c = a[:]
print("Lista c (copia de a usando slicing):", c)
c[0] = 10
print("Después de modificar el primer elemento de 'c':")
print("Lista a:", a)
print(id(a))
print("Lista b:", b)
print(id(b))
print("Lista c:", c)
print(id(c))
# En este caso, 'c' es una copia de 'a' creada usando slicing.
# Ahora 'c' es una copia de 'a', y modificar 'c' no afecta a 'a' ni a 'b'.
