n = 20
w = "Weird"
nw = "Not Weird"
if n % 2 == 1:
    print(w)
    print("Odd number")
elif range(2,6) or n>20:
    print(nw)
    print("Even number range 2 to 5 or greater than 20")
elif range(5,21):
    print(w)
    print("Even number in range 5 to 20")
else:
    print(nw)
    print("Even number")

def is_leap(year):
    leap = False
    if year % 400 == 0:
        leap = True
    return leap
year = int(input())
print(is_leap(year))
# This code demonstrates how to check if a year is a leap year.

def mutate_string(string, position, character):
    return

if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)