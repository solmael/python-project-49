from random import randint

DESCRIPTION = 'What number is missing in the progression?'


def generate_round_data():
    start = randint(1, 99)
    step = randint(1, 10)
    length = 10
    progression = [start + step * i for i in range(length)]
    index_missed_num = randint(0, length - 1)
    missed_num = str(progression[index_missed_num])
    progression[index_missed_num] = '..'
    progression_str = ' '.join(str(num) for num in progression)
    return progression_str, missed_num
