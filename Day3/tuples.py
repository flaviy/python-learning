my_tuple = (1, 2, 3, 4, 5, 'testst', 1)
print(type(my_tuple))  # <class 'tuple'>
my_tuple2 = 1, 2, 3, 4, 5, 'testst', 1
print(my_tuple2)
print(my_tuple[-2])  # testst
print(my_tuple[2:5])  # (3, 4, 5)
my_complex_tuple = (1, 2, 3, 4, 5, 'testst', 1, (1, 2, 3, 4, 5, 'testst', 1))
print(my_complex_tuple[-1][5])  # testst

# convert tuple to list (casting)
my_list = list(my_tuple)
print(type(my_list))  # <class 'list'>
print(my_list)  # [1, 2, 3, 4, 5, 'testst', 1]

# and vice versa (casting)
my_tuple = tuple(my_list)
print(type(my_tuple))  # <class 'tuple'>
print(my_tuple)  # (1, 2, 3, 4, 5, 'testst', 1)

# similarly like in php we can unpack tuple
a, b, c, d, e, f, g = my_tuple
print(a)  # 1
print(b)  # 2
print(c, d)  # 3 4

# you can also use the * operator to unpack the rest of the elements
a, b, *c = my_tuple
print(a)  # 1
print(b)  # 2
print(c)  # [3, 4, 5, 'testst', 1]

print(len(my_tuple))  # 7

# count the number of occurrences of an element in a tuple
print(my_tuple.count(1))  # 2

# it is also possible for lists
my_list = [1, 2, 3, 4, 5, 'testst', 1]
print(my_list.count(1))  # 2

# find the index of an element in a tuple
print(my_tuple.index(1))  # 0

#it is also possible to check if element is in a tuple
print(1 in my_tuple)  # True
