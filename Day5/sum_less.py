# numbers = [1, 200, 10000, 2, -2, 20000]
#
# def sum_less(numbers):
#     sum = 0
#     i = 0
#     while i < len(numbers):
#         if (numbers[i] > 0 and numbers[i] < 1000):
#             sum += numbers[i]
#             print(f"adding {numbers[i]} to sum")
#         else:
#             print(f"Skipping {numbers[i]} - don't add to sum")
#         i += 1
# sum_less(numbers)


numbers = [1, 200, 10000, 2, -2, 20000]

def sum_less(numbers):
    total = sum(num for num in numbers if 0 < num < 1000)
    print(f"The total sum of numbers between 0 and 1000 is {total}")

sum_less(numbers)
