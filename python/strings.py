## This code demonstrates the use of strings in Python, and shows which type of data is used to represent strings. 
name = "David"
print(type(name))

# This code prints the first character of the string stored in the variable 'name'.
print(name[0])

# This code prints teh combination or concatenation of two strings.
lastname = "Augusto Trujillo Delgado"
print(name + " " + lastname)

# This code prints the length of the string stored in the variable 'name'.
print(len(name))

# This code demonstrates the method lower() which converts all characters in the string to lowercase.
print(name.lower)

# This code demonstrates various string methods in Python.

# .count() - Returns the number of occurrences of a substring in the string.
print(name.count("a"))

# .capitalize() - Returns a copy of the string with its first character capitalized.
print(name.capitalize())

# .title() - Returns a titlecased version of the string, where each word starts with an uppercase character.
print(name.title())

# .swapcase() - Returns a copy of the string with uppercase characters converted to lowercase and vice versa.
print(name.swapcase())

# .replace() - Returns a copy of the string with all occurrences of a substring replaced by another substring.
print(name.replace("a", "o"))

# .split() - Splits the string into a list where each word is a list item.
print(name.split())

# .strip() - Returns a copy of the string with leading and trailing whitespace removed.
print(name.strip())

# .lstrip() - Returns a copy of the string with leading whitespace removed.
print(name.lstrip())

# .rstrip() - Returns a copy of the string with trailing whitespace removed.
print(name.rstrip())

# .find() - Returns the lowest index of the substring if found in the string. Returns -1 if not found.
print(name.find("a"))

# .index() - Returns the lowest index of the substring if found in the string. Raises an error if not found.
print(name.index("a"))

# eval() - Evaluates the specified expression if the string contains a valid Python expression.
# WARNING: Using eval() can be dangerous if the input is not trusted.
# print(eval("2 + 2"))

# exec() - Executes the dynamically created Python program which is either a string or object code.
# WARNING: Using exec() can be dangerous if the input is not trusted.
# exec("print('Hello from exec')")