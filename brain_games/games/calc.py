from brain_games.const import CALC_INSTRUCTION
from brain_games.engine import start_game
from brain_games.random_utils import get_math_signs_and_operator, get_random_num


def get_expression_and_result():
    num1, num2 = get_random_num(), get_random_num() # random integer from 1 to 99
    math_signs, random_sign = get_math_signs_and_operator() # math_signs values is +, -, *
    expression = f'{num1} {random_sign} {num2}'
    result = (math_signs[random_sign](num1, num2))
    return expression, str(result)


def run_game_calc():
    start_game(get_expression_and_result, CALC_INSTRUCTION)
