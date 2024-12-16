from random import randint
from brain_games.const import PROGRESSION_INSTRUCTION
from brain_games.engine import start_game


def get_progression_and_result():
    start = randint(1, 100)
    step = randint(1, 10)
    length = 10
    progression = [start + step * i for i in range(length)]
    index_missed_num = randint(0, length - 1)
    missed_num = str(progression[index_missed_num])
    progression[index_missed_num] = '..'
    progression_str = ' '.join(str(num) for num in progression)

    return progression_str, missed_num


def run_game_progression():
    start_game(get_progression_and_result, PROGRESSION_INSTRUCTION)
