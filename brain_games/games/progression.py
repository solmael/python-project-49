import random

from brain_games.engine import start_game
from brain_games.const import PROGRESSION_INSTRUCTION


def get_progression_and_result():
    start = random.randint(1, 100)
    step = random.randint(1, 10)
    length = 10
    progression = [start + step * i for i in range(length)]
    index_missed_num = random.randint(0, length - 1)
    missed_num = str(progression[index_missed_num])
    progression[index_missed_num] = '..'
    progression_str = ' '.join(str(num) for num in progression)

    return progression_str, missed_num


def run_game_progression():
    start_game(get_progression_and_result, PROGRESSION_INSTRUCTION)
