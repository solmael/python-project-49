from brain_games.const import PROGRESSION_INSTRUCTION
from brain_games.engine import start_game
from brain_games.random_utils import (
    get_random_length_indx,
    get_random_num,
    get_random_num_small,
)


def get_progression_and_result():
    start = get_random_num()  # random int from 1 to 99
    step = get_random_num_small()  # random int from 1 to 10
    length = 10
    progression = [start + step * i for i in range(length)]
    index_missed_num = get_random_length_indx()
    missed_num = str(progression[index_missed_num])
    progression[index_missed_num] = '..'
    progression_str = ' '.join(str(num) for num in progression)

    return progression_str, missed_num


def run_game_progression():
    start_game(get_progression_and_result, PROGRESSION_INSTRUCTION)
