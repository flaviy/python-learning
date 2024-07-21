from random import randint, choice


def throw_dice():
    try_one = randint(1, 6)
    try_two = randint(1, 6)
    return try_one, try_two


def roll_result(try_one, try_two):
    sum_dice = try_one + try_two
    if sum_dice <= 6:
        message = f"The sum of your dice is {sum_dice}. Unfortunate"
    elif sum_dice <= 9:
        message = f"The sum of your dice is {sum_dice}. You have a good chance"
    else:
        message = f"The sum of your dice is {sum_dice}. It looks like a winning roll!"
    return message


result = throw_dice()
print(roll_result(result[0], result[1]))

numbers = [1, 2, 3, 5, 0, 333, 4, 1, 2]


def reduce_list(numbers):
    unique_numbers = set(numbers)
    highest = max(unique_numbers)
    unique_numbers.discard(highest)
    return list(unique_numbers)


def average(numbers):
    return sum(numbers) / len(numbers)


print(average(reduce_list(numbers)))

secret_codes = ['23423423', 'sdfdsfdsfds', 'w4erewrewrwe', 'werewrewr']


def toss_coin():
    return choice(['Heads', 'Tails'])


def lucky_coin(toss, secret_codes):
    if toss == 'Heads':
        print("List was saved")
        return secret_codes
    else:
        print("List will self-destruct")
        return []


lucky_coin(toss_coin(), secret_codes)
