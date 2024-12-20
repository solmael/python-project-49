from operator import add, mul, sub
from random import choice, randint

DESCRIPTION = 'What is the result of the expression?'


def generate_round_data():
    num1, num2 = randint(1, 10), randint(1, 10)
    math_signs = {'+': add, '-': sub, '*': mul}
    random_sign = choice(list(math_signs.keys()))
    expression = f'{num1} {random_sign} {num2}'
    result = math_signs[random_sign](num1, num2)
    return expression, str(result)
