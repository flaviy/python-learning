my_string = 'Letter'
print(min(my_string))  # L, because python searches between upper case letters first

print((min(my_string.lower()))) # now it's e

my_dict = {'key1': 10, 'key2': 22, 'key3': 3}
print(min(my_dict))  # key1, because python searches between keys

print(min(my_dict.values()))  # 3, to search between values, we need to use min(my_dict.values())

# how to show the key of the minimum value
print(min(my_dict, key=my_dict.get))  # key3, get() method returns the value of the specified key, so it will return the key of the minimum value