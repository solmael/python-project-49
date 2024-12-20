from math import gcd
from random import randint

DESCRIPTION = 'Find the greatest common divisor of given numbers.'


def generate_round_data():
    num1, num2 = randint(1, 99), randint(1, 99)
    result = str(gcd(num1, num2))
    couple_nums = f'{num1} {num2}'
    return couple_nums, result
