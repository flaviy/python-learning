def greeting():
    """
    This function prints "Hello, World!" to the console.
    :return:
    """
    print("Hello, World!")


print(greeting.__doc__)  # This function prints "Hello, World!" to the console.
greeting()  # Hello, World!


def welcome(name):
    print(f'Welcome {name}!')


welcome("John")  # Welcome John!
