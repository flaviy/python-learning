#from random import randint
from random import *

randint = randint(1, 100) # random integer between 1 and 100, 100 included, 1 included
print(randint)

my_random = uniform(1, 100) # random float between 1 and 100 , e.g 96.25687646349564

print(round(my_random, 2)) # round to 2 decimal places

my_random= random() # random float between 0 and 1
print(my_random) # e.g. 0.1234567890123456

my_random = choice(['a', 'b', 'c', 'd']) # random choice from the list
print(my_random) # e.g. 'a'

numbers = list(range(5, 50, 5))
print(numbers) # [5, 10, 15, 20, 25, 30, 35, 40, 45]

shuffle(numbers) # shuffle the list
print(numbers) # e.g. [45, 5, 35, 15, 25, 10, 40, 20, 30]
