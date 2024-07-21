word = 'python'
my_list = []
for letter in word:
    my_list.append(letter)
print(my_list)

# list comprehension
my_list = [letter for letter in word] # it's the same as the for loop above, but in one line
print(my_list)

my_lst = [n for n in range(1, 11, 2)]
print(my_lst)

my_lst = [n + 3 if n % 2 != 0 else None for n in range(1, 11)]
print(my_lst)
feet  = [10, 20, 30, 40]
meters = [f * 0.3048 for f in feet]

print(meters)