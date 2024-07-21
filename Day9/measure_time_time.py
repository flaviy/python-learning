import time
'''
 Time is not accurate enough for measuring small time intervals.
'''

def for_test(number):
    my_list = []
    for i in range(1, number + 1):
        my_list.append(i)
    return my_list


def while_test(number):
    my_list = []
    i = 1
    while i <= number:
        my_list.append(i)
        i += 1
    return my_list


begin = time.time()
for_test(10000000)
end = time.time()
print(end - begin)

begin = time.time()
while_test(10000000)
end = time.time()

print(end - begin)

