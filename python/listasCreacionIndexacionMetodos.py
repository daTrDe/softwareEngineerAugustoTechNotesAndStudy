to_do = ["Dirigirnos al hotel",
       "Ir por una chela",
       "Visitar un museo",
       "Volver al hotel"]
print(to_do)
numbers = [1, 2, 3, 4, "cinco"]
print(numbers)
print(type(numbers))  # This will show the type of the variable 'numbers', which is a list. 
mix = ["uno", 1, 3.14, True, [1,2,3]]
print(mix)
print(len(mix))  # This will print the length of the list 'mix', which is 5.
print("Primer elemento de la lista mix:", mix[0])  # This will print the first element of the list 'mix'.
print("Segundo elemento de la lista mix:", mix[1])  # This will print the second element of the list 'mix'.
print("Último elemento de la lista mix:", mix[-1])  # This will print the last element of the list 'mix'.
print(type(mix))  # This will show the type of the variable 'mix', which is a list containing mixed data types.
print(mix[:2])  # This will print the first two elements of the list 'mix'.
print(mix[1:3])  # This will print the second and third elements of the list 'mix'.
mix.append(False)  # This will append the boolean value False to the end of the list 'mix'.
print("Lista mix después de append:", mix)  # This will print the list 'mix' after appending False.
mix.insert(2, "dos")  # This will insert the string "dos" at index 2 of the list 'mix'.
print("Lista mix después de insert:", mix)  # This will print the list 'mix' after inserting "dos" at index 2.
mix.index("uno")  # This will return the index of the first occurrence of the string "uno" in the list 'mix'.
print("Índice de 'uno' en mix:", mix.index("uno"))  # This will print the index of the first occurrence of "uno" in the list 'mix'.
mix.remove("uno")  # This will remove the first occurrence of the string "uno" from the list 'mix'.
print("Lista mix después de remove:", mix)  # This will print the list 'mix' after removing "uno".
mix.pop()  # This will remove and return the last element of the list 'mix'.
print("Lista mix después de pop:", mix)  # This will print the list 'mix' after popping the last element.
mix.clear()  # This will remove all elements from the list 'mix'.
print("Lista mix después de clear:", mix)  # This will print the list 'mix' after clearing all elements.
mix = ["uno", 1, 3.14, True, [1,2,3]]
