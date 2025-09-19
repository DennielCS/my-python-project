import sys # for CH04
import datetime # for CH04 pt 2

print("Hello, Git!")

# Exercises

# CH04
# User Story: Converts variables

text = '7.2'
number       = float(text) # value = 7.2
whole_number = int(number) # value = 7
print(number, whole_number)


print(f"The current version of Python is {sys.version}")
print(f"The whole number of 7.2 is {whole_number}")

# User Story: Ask a number then provides a square and cube root of it.

given = input("Type any number: ")
square = int(given)**2
cube = int(given)**3
print(f"The square root of {given} is {square}")
print(f"The cube root of {given} is {cube}")

# CH04 pt 2
# User Story: Ask user for name and age. tells how many years you are olden than the user

name = input("Enter your name: ")
age = (int(input("Enter your age: ")))
date = datetime.date.today()
vsAge = age - 18


if age < 18:
    print(f"{name} is {vsAge} years younger than me")
else:
    print(f"{name} is {age} years old ({date}) and {vsAge}  years older than me")


# CH05
# User Story: Ask a number then identifies if its even or odd

attempts = 0

while True:
    num = int(input("Enter a number: "))
    remainder = num % 2

    if num == 0:
        print("Goodbye!")
        break
    attempts += 1

    if num % 2 == 0:
        print("Even")
    else:
        print("Odd")








