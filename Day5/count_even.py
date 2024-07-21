#num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# def count_even(num):
#     count = 0
#     for i in num:
#         if i % 2 == 0:
#             count += 1
#     return count
# print(count_even(num))


num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def count_even(num):
    print([i for i in num if i % 2 == 0])
    return len([i for i in num if i % 2 == 0])

print(count_even(num))

