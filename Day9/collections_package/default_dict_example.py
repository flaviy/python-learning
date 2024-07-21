from collections import defaultdict


def example():
    my_usual_dict = {'one': 'green', 'two': 'blue', 'three': 'red'}
    print(my_usual_dict['one'])  # green
    try:
        print(my_usual_dict['four'])
    except KeyError as e:
        print('Error occurred : KeyError')
        print(f'{e} - key not found')

    my_dict = defaultdict(lambda: 'No such key')
    my_dict['one'] = 'green'
    my_dict['two'] = 'blue'

    print(my_dict['one'])  # green
    print(my_dict['four'])  # No such key
    print(my_dict)  # defaultdict(<function example.<locals>.<lambda> at 0x7f8f3c1b7d30>, {'one': 'green', 'two': 'blue', 'four': 'No such key'})
