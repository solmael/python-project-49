from random import randint

DESCRIPTION = 'Answer "yes" if the number is even, otherwise answer "no".'


def is_even(num):
    return num % 2 == 0


def generate_round_data():
    num = randint(1, 99)
    answer = 'yes' if is_even(num) else 'no'
    return num, answer
