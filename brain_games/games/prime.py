from brain_games.const import PRIME_INSTRUCTION
from brain_games.engine import start_game
from brain_games.random_utils import get_random_num


def is_prime(num):
    if num < 2:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True


def get_num_and_answer():
    num = get_random_num()
    answer = 'yes' if is_prime(num) else 'no'

    return num, answer


def run_game_prime():
    start_game(get_num_and_answer, PRIME_INSTRUCTION)
