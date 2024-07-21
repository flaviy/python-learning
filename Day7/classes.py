class Bird:
    pass


bird1 = Bird()
bird2 = Bird()

print(bird1)
print(bird2)

print(type(bird1))  # <class '__main__.Bird'>


class Car:
    is_auto = True  # class attribute

    def __init__(self, brand, model, year):
        self.brand = brand  # instance attribute
        self.model = model  # instance attribute
        self.year = year  # instance attribute

    def __str__(self):
        return f'{self.brand} {self.model} {self.year}'

    def ride(self, km):
        print(f'The car of brand {self.brand} rides {km} km')


my_car = Car('Toyota', 'Corolla', 2015)
print(my_car)  # Toyota Corolla 2015

print(my_car.is_auto)  # True
print(Car.is_auto)  # True
my_car.ride(100)  # The car of brand Toyota rides 100 km


class Animal:
    def __init__(self, color, age):
        self.color = color
        self.age = age

    def born(self):
        print('The animal is born')


class Bird(Animal):
    def __init__(self, color, age, wingspan):
        super().__init__(color, age)  # calling the parent class constructor

    def born(self):
        print('The bird is born')


print(issubclass(Bird, Animal))  # True
print(issubclass(Bird, object))  # True
print(Bird.__bases__)  # (<class '__main__.Animal'>,)
print(Animal.__bases__)  # (<class 'object'>,)
print(object.__bases__)  # ()
print(Animal.__subclasses__())  # [<class '__main__.Bird'>]

tweet = Bird('blue', '2 years', '30 cm')
tweet.born()  # The bird is born
print(tweet.color)  # blue
