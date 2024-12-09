import random

from brain_games.const import CALC_INSTRUCTION, MATH_SIGNS
from brain_games.engine import start_game


def get_expression_and_result():
    num1, num2 = random.randint(1, 100), random.randint(1, 100)
    sign = random.choice(MATH_SIGNS)
    expression = f'{num1} {sign} {num2}'
    result = str(eval(expression))
    return expression, result


def run_game_calc():
    start_game(get_expression_and_result, CALC_INSTRUCTION)
