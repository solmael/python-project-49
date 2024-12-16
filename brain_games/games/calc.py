from random import randint, choice
from operator import add, sub, mul
from brain_games.const import CALC_INSTRUCTION
from brain_games.engine import start_game


def get_expression_and_result():
    num1, num2 = randint(1, 10), randint(1, 10)
    math_signs = {'+': add, '-': sub, '*': mul}
    random_sign = choice(list(math_signs.keys()))
    expression = f'{num1} {random_sign} {num2}'
    result = (math_signs[random_sign](num1, num2))
    return expression, str(result)


def run_game_calc():
    start_game(get_expression_and_result, CALC_INSTRUCTION)
