from collections import namedtuple


def example():
    my_tuple = (10, 20, 30)
    print(my_tuple[0])  # 10

person = namedtuple('Person', ['name', 'height', 'weight'])
michael = person('Michael', 180, 70)
print(michael.name)  # Michael

john = person('John', 175, 65)
print(john.height)  # 175

