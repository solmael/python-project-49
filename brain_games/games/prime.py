from random import randint

DESCRIPTION = (
    'Answer "yes" if given number is prime. Otherwise answer "no".'
)

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def get_num_and_answer():
    print(DESCRIPTION)
    num = randint(1, 99)
    answer = 'yes' if is_prime(num) else 'no'
    return num, answer
