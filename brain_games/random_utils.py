from operator import add, mul, sub
from random import choice, randint


def get_random_num():
    return randint(1, 99)


def get_random_num_small():
    return randint(1, 10)


def get_random_length_indx():
    return randint(0, 9)


def get_math_signs_and_operator():
    math_signs = {'+': add, '-': sub, '*': mul}
    operator = choice(list(math_signs.keys()))
    return math_signs, operator
