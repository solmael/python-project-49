from brain_games.const import EVEN_INSTRUCTION
from brain_games.engine import start_game
from brain_games.random_utils import get_random_num


def is_even(num):
    return num % 2 == 0


def get_num_and_answer():
    num = get_random_num()
    answer = 'yes' if is_even(num) else 'no'

    return num, answer


def run_game_even():
    start_game(get_num_and_answer, EVEN_INSTRUCTION)
