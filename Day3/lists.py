print(type([1, 2, 3]))  # <class 'list'>
my_list = [1, 2, 3]

result_length = len(my_list)
print(result_length)  # 3
my_list2 = my_list[0:2]
print(my_list2)  # [1]
my_list3 = my_list[1:3] # it means from 1 to 3, but 3 is not included
print(my_list3)  # [2, 3]
my_list4 = my_list[1:]  # it means from 1 to the end
print(my_list4)  # [2, 3]
my_list5 = my_list[:2]  # it means from the beginning to 2
print(my_list5)  # [1, 2]
my_list_6 = my_list + my_list5
print(my_list_6)  # [1, 2, 3, 1, 2]

#  append method
my_list_6.append(4444)
print(my_list_6)  # [1, 2, 3, 1, 2, 4444]

# pop method
my_list_6.pop() # it will remove the last element from the list
print(my_list_6)  # [1, 2, 3, 1, 2]
my_list_6.pop(2)  # it will remove the element at index 2
print(my_list_6)  # [1, 2, 1, 2]
deleted = my_list_6.pop(2)  # it will remove the element at index 2 and assign it to deleted
print(deleted)  # 1
print(my_list_6)  # [1, 2, 2]

# sort and reverse methods
unordered_list = ['a', 'c', 'e', 'd', 'b', 'o']
unordered_list.sort()  # it will sort the list in ascending order
print(unordered_list)  # ['a', 'b', 'c', 'd', 'e', 'o']
unordered_list.reverse()  # it will reverse the list
print(unordered_list)  # ['o', 'e', 'd', 'c', 'b', 'a']

