from math import gcd

from brain_games.const import GCD_INSTRUCTION
from brain_games.engine import start_game
from brain_games.random_utils import get_random_num


def get_nums_and_result():
    num1, num2 = get_random_num(), get_random_num()
    result = str(gcd(num1, num2))
    couple_nums = f'{num1} {num2}'

    return couple_nums, result


def run_game_gcd():
    start_game(get_nums_and_result, GCD_INSTRUCTION)
