for n in range(5):
    print(n)  # 0 1 2 3 4

for n in range(2, 5):
    print(n)  # 2 3 4

for n in range(2, 10, 2):
    print(n)  # 2 4 6 8

for n in range(10, 2, -4):
    print(n)  # 10 6,  # 2 is not included

my_list = range(1, 5) # it will create a range object
print(type(my_list))  # <class 'range'>
print(list(my_list))  # [1, 2, 3, 4]