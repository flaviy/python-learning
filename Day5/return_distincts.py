
#  first solution
def return_distincts(num1, num2, num3):
    sum_of_nums = num1 + num2 + num3
    list_of_nums = [num1, num2, num3]
    if sum_of_nums > 15:
        return max(list_of_nums)
    elif sum_of_nums < 10:
        return min(list_of_nums)
    else:
        return sum_of_nums - max(list_of_nums) - min(list_of_nums)


print(return_distincts(8, 2, 3))


# another solution

def return_different_values(a, b, c):

    a_sum = a + b + c
    a_list = [a, b, c]

    if a_sum > 15:
        return max(a_list)
    elif a_sum < 10:
        return min(a_list)
    else:
        a_list.sort()
        return a_list[1]


print(return_different_values(3, 2, 7))