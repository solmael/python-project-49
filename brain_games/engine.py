import prompt
from brain_games.cli import welcome_user
from brain_games.const import NUM_OF_ROUNDS


def start_game(get_question_and_answer, instruction):
    name = welcome_user()
    print(f'{instruction}')
    for _ in range(NUM_OF_ROUNDS):
        question, answer = get_question_and_answer()
        print(f'Question: {question}')
        user_answer = prompt.string('Your answer: ')
        if user_answer == answer:
            print('Correct!')
        else:
            print(f"'{user_answer}' is wrong answer ;(. "
                  f"Correct answer was '{answer}'.\n"
                  f"Let's try again, {name}!")
            return
    print(f'Congratulations, {name}!')
