def check_if_consequent_zero(*args):

    for key, value in enumerate(args):
        if value == 0:
            # check the next value exists and is equal to 0
            try:
                if args[key + 1] == 0:
                    return True
            except IndexError:
                break
    return False


print(check_if_consequent_zero(1, 2, 2, 3, 4, 2, 3, 2, 0,1,0))


# another way to solve this problem

def neighboring_zeros(*args):
    counter = 0

    for n in args:

        if counter + 1 == len(args):
            return False
        elif args[counter] == 0 and args[counter + 1] == 0:
            return True
        else:
            counter += 1

    return False


print(neighboring_zeros(0, 4, 0, 8, 1, 3, 9, 8, 0, 2, 0))
