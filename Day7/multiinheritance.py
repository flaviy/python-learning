class Father:
    def __init__(self):
        print("Father class constructor is called")

    def laugh(self):
        print("Father is laughing")


class Mother:
    def __init__(self):
        print("Mother class constructor is called")

    def laugh(self):
        print("Mother is laughing")


class Child(Father, Mother):
    def __init__(self):
        print("Child class constructor is called")
        super().__init__()


child = Child()  # Child class constructor is called # Father class constructor is called
child.laugh()  # Father is laughing

# The Child class inherits from both Father and Mother classes. The Child class constructor
# is called first, then the Father class constructor is called. The laugh method of the Father

print(Child.__bases__)  # (<class '__main__.Father'>, <class '__main__.Mother'>)
print(issubclass(Child, Father))  # True
print(Child.__mro__)  # (<class '__main__.Child'>, <class '__main__.Father'>, <class '__main__.Mother'>, <class 'object'>)