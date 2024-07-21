def sum_args(*args):
    return sum(args)


print(sum_args(1, 2, 3, 4, 5))  # 15

'''
<?php

function sum_args(...$args) {
    return array_sum($args);
}

echo sum_args(1, 2, 3, 4, 5);  // Outputs: 15

?>
'''


def sum_squares(*args):
    return sum(arg ** 2 for arg in args)


print(sum_squares(1, 2, 3, 4, 5))  # 55


def absolute_sum(*args):
    return sum(abs(arg) for arg in args)


print(absolute_sum(-1, -22, -3, -4, -5))  # 15
