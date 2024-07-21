import timeit

declaration = """
for_test(10)
"""

my_setup = """
def for_test(number):
    my_list = []
    for i in range(1, number + 1):
        my_list.append(i)
    return my_list
"""

length = timeit.timeit(setup=my_setup, stmt=declaration, number=1000000)
print(length)


declaration2 = """
while_test(10)
"""

my_setup2 = """
def while_test(number):
    my_list = []
    i = 1
    while i <= number:
        my_list.append(i)
        i += 1
    return my_list
"""

length2 = timeit.timeit(setup=my_setup2, stmt=declaration2, number=1000000)

print(length2)
