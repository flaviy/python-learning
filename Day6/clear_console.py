from os import system

name = input("Enter your name: ")
print(f"Hello, {name}!")

age = input("Enter your age: ")


# Try to clear the console
if system('cls') != 0:  # If 'cls' command fails (non-zero status)
    system('clear')  # Try 'clear' command

print(f"You are {age} years old.")