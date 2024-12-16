import prompt

from brain_games.const import NUM_OF_ROUNDS
from brain_games.cli import welcome_user


def start_game(get_question_and_answer, instruction):
    name = welcome_user()
    print(f'{instruction}')
    for _ in range(NUM_OF_ROUNDS):
        question, answer = get_question_and_answer()
        user_answer = prompt.string(f'Question: {question}\n'
                                    f'Your answer: ')
        if user_answer == answer:
            print('Correct!')
        else:
            print(f"'{user_answer}' is wrong answer ;(. "
                  f"Correct answer was '{answer}'.\n"
                  f"Let's try again, {name}!")
            return False
    print(f'Congratulations, {name}!')
