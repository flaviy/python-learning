for a, b in [(1, 2), (3, 4), (5, 6)]:
    print(a, b)  # 1 2 3 4 5 6

for a, b in [[1, 2], (3, 4), (5, 6)]:
    print(a)  # 1 3 5
    print(b)  # 2 4 6

for a in [(1, 2), (3, 4), (5, 6)]:
    print(a)  #  (1, 2) (3, 4) (5, 6)

for a in "wordoftanks":
    print(a)  # w o r d o f t a n k s

dic = {'a': 1, 'b': 2, 'c': 3}
for key, value in dic.items():
    print(key, value)  # a 1 b 2 c 3

for key in dic.keys():
    print(key)  # a b c

for key in dic:
    print(key)  # a b c

for value in dic.items():
    print(value)  # ('a', 1) ('b', 2) ('c', 3)

for value in dic.values():
    print(value)  # 1 2 3

