from random import shuffle

#initial list

sitcks = ['-', '--', '---', '----']


#mixing sticks
def mix(my_list):
    shuffle(my_list)
    return my_list


print(mix(sitcks))


def try_your_luck(my_list):
    #mixing sticks
    my_list = mix(my_list)
    #taking one stick from the beginning of the list
    stick = my_list.pop()
    return stick


def verify_your_luck(sticks):
    if len(try_your_luck(sticks)) == 1:
        print("You took the shortest!")
    else:
        print("You didn't take the shortest!")


verify_your_luck(sitcks)
