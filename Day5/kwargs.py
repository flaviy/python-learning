def a_sum(**kwargs):
    print(type(kwargs))  # <class 'dict'>
    print(kwargs['c'])  # 3
    print(type(kwargs.items()))  # <class 'dict_items'>
    for key, value in kwargs.items():
        print(key, value)

    return sum(kwargs.values())


a_sum(a=1, b=2, c=3, d=4, e=5)  # 15


def test(name, value, *args, **kwargs):
    print(name, value)
    for arg in args:
        print(arg)
    for key, value in kwargs.items():
        print(key, value)


dogs = {'terier': 'burek', 'bulldog': 'rex', 'poodle': 'fluffy'}
dogs_list = ['burek', 'rex', 'fluffy']

test('test', 1, *dogs_list, **dogs) # test 1 burek rex fluffy terier burek bulldog rex poodle fluffy


def list_attributes(**kwargs):
    #return list of the values of the dictionary
    return list(kwargs.values())


def describe_person(name, **kwargs):
    print(f'Characteristics of {name}:')
    print(type(kwargs))  # <class 'dict'>
    print(type(kwargs.items()))  # <class 'dict_items'>

    for argument_name, argument_value in kwargs.items():
        print(f'{argument_name}: {argument_value}')

describe_person('John', age=30, height=180, weight=80) # Characteristics of John: age: 30 height: 180 weight: 80
