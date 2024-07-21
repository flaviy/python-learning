my_set = set([1, 2, 3, 4, 5])
print(my_set)  # {1, 2, 3, 4, 5}
print(type(my_set))  # <class 'set'>
my_set_2 = {1, 2, 3, 4, 5, 1, 2, 3, 4, 5}
print(my_set_2)  # {1, 2, 3, 4, 5} # duplicates are removed
# get the length of a set
print(len(my_set))  # 5
# add an element to a set (it is not possible to add an element at a specific index)
my_set.add(6)
print(my_set)  # {1, 2, 3, 4, 5, 6}

# remove an element from a set
my_set.remove(6)
print(my_set)  # {1, 2, 3, 4, 5}

# get the difference between two sets
my_set_3 = {1, 2, 3, 4, 5, 6}
my_set_4 = {1, 2, 3, 4, 5}
difference = my_set_3 - my_set_4
print(difference)  # {6}

# get the intersection of two sets
intersection = my_set_3 & my_set_4
print(intersection)  # {1, 2, 3, 4, 5}

# get the union of two sets - it mean all elements from both sets, but duplicates are removed
union = my_set_3 | my_set_4
print(union)  # {1, 2, 3, 4, 5, 6}

# check if a set is a subset of another set
print(my_set_4.issubset(my_set_3))  # True
print(my_set_3.issubset(my_set_4))  # False

# get second element from the set
print(list(my_set_3)[1])  # 2 it is not possible to get an element by index from a set

#sets could include tuples, because tuples are immutable
#tuple - is a collection which is ordered and unchangeable
my_set_5 = {(1, 2), (3, 4), (5, 6)}
print(my_set_5)  # {(1, 2), (3, 4), (5, 6)}

#check if an element is in a set
print(1 in my_set)  # True

#the same as in lists, you can use the * operator to unpack the rest of the elements
a, *b = my_set
print(a)  # 1
print(b)  # [2, 3, 4, 5]

#it is also possible to use the add method to add multiple elements to a set
my_set.add(7)
print(my_set)  # {1, 2, 3, 4, 5, 7}
my_set.update([8, 9, 10])
print(my_set)  # {1, 2, 3, 4, 5, 7, 8, 9, 10}

#remove multiple elements from a set
my_set.remove(8)
my_set.remove(9)

print(my_set)  # {1, 2, 3, 4, 5, 7, 10}

#use discard method to remove an element from a set, if the element is not in the set, it will not raise an error
my_set.discard(10)
print(my_set)  # {1, 2, 3, 4, 5, 7}

#pop method removes a random element from a set
my_set.pop()
print(my_set)  # {2, 3, 4, 5, 7}

#clear method removes all elements from a set
my_set.clear()
print(my_set)  # set()

