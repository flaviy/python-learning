from collections import Counter


def example():

    # Counter is a dictionary subclass that counts hashable objects
    numbers = [1, 2, 3, 4, 1, 2, 3, 1, 2, 1]
    count = Counter(numbers)
    print(count)  # Counter({1: 4, 2: 3, 3: 2, 4: 1})

    print(count[1])  # 4

    print(Counter('abracadabra'))  # Counter({'a': 5, 'b': 2, 'r': 2, 'c': 1, 'd': 1}

    sentence = 'The quick brown fox lazy jumps over the lazy dog fox dog fox'
    words = sentence.split()
    word_count = Counter(words)
    print(word_count)  # Counter({'The': 1, 'quick': 1, 'brown': 1, 'fox': 1, 'jumps': 1, 'over': 1, 'the': 1, 'lazy': 1, 'dog': 1})
    print(word_count.items())  # dict_items([('The', 1), ('quick', 1), ('brown', 1), ('fox', 1), ('lazy', 2), ('jumps', 1), ('over', 1), ('the', 1), ('dog', 1)])
    print(word_count.keys())  # dict_keys(['The', 'quick', 'brown', 'fox', 'lazy', 'jumps', 'over', 'the', 'dog'])
    print(word_count.values())  # dict_values([1, 1, 1, 1, 2, 1, 1, 1, 1])
    print(word_count.most_common(3))
    print(word_count.most_common())  # [('fox', 3), ('lazy', 2), ('dog', 2), ('The', 1), ('quick', 1), ('brown', 1),
    # ('jumps', 1), ('over', 1), ('the', 1)]

