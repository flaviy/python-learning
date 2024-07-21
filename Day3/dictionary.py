my_dictionary = {'name': 'John', 'age': 26, 'city': 'New York'}
print(type(my_dictionary))  # <class 'dict'>
result = my_dictionary['name']
print(result)  # John

dic = {1: 44, 2: [2, 3, 4], 3: 'hello', 4: {'name': 'John', 'age': 26}}
print(dic)  # {1: 44, 2: [2, 3, 4], 3: 'hello', 4: {'name': 'John', 'age': 26}}
print(dic[2][1])  # 3
print(dic[4]['name'])  # John
print(dic[3][:2])
dic['test'] = 'test'
print(dic)  # {1: 44, 2: [2, 3, 4], 3: 'hello', 4: {'name': 'John', 'age': 26}, 'test': 'test'}
print(type(dic.keys()))  # dict_keys([1, 2, 3, 4, 'test'])
print(type(dic.values()))  # dict_values([44, [2, 3, 4], 'hello', {'name': 'John', 'age': 26}, 'test'])
print(dic.keys())  # dict_keys([1, 2, 3, 4, 'test'])
print(dic.values())  # dict_values([44, [2, 3, 4], 'hello', {'name': 'John', 'age': 26}, 'test'])
print(dic.items())  # dict_items([(1, 44), (2, [2, 3, 4]), (3, 'hello'), (4, {'name': 'John', 'age': 26}), ('test', 'test')])
print(dic.get(2))  # [2, 3, 4], get() method returns the value of the specified key

print(dic.items())  # dict_items([(1, 44), (2, [2, 3, 4]), (3, 'hello'), (4, {'name': 'John', 'age': 26}), ('test', 'test')])