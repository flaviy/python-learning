for item in enumerate(range(5)):
    print(item)  # (0, 0) (1, 1) (2, 2) (3, 3) (4, 4)

for index, value in enumerate(range(5)):
    print(index, value)  # 0 0 1 1 2 2 3 3 4 4

for index, value in enumerate(["a", "b", "c", "d"]):
    print(index, value)  # 0 a 1 b 2 c 3 d

my_list = ["a", "b", "c", "d"]
print(enumerate(my_list))  # <enumerate object at 0x7f9c9f1c9b40>
my_tuples = list(enumerate(my_list))
print(my_tuples)  # [(0, 'a'), (1, 'b'), (2, 'c'), (3, 'd')]
print(type(my_tuples))  # <class 'list'>
print(type(my_tuples[2]))  # <class 'tuple'>
