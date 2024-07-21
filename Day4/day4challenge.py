from random import randint

attempts = 8
random_value = randint(1, 100)
print("Well John, I've thought of a number between 1 and 100 and you \n" +
      "have only eight tries to guess it. What number do you think it is?")

while attempts > 0:

    user_input = input(f"You have {attempts} attempts left. Enter your number: ")
    attempts -= 1
    if not user_input.isdecimal():
        print("Please enter a valid number")
        continue
    user_input = int(user_input)
    if user_input > 100 or user_input < 1:
        print("Chosen a key number that is out of play")
    elif user_input < random_value:
        print("The key number is higher")
    elif user_input > random_value:
        print("The key number is lower")
    else:
        print("Congratulations! You guessed the key number")
        print(f"You have guessed the key number in {8 - attempts} attempts")
        break
else:
    print("You have no more attempts. The key number was :", random_value)
