import prompt

from brain_games.cli import welcome_user

NUM_OF_ROUNDS = 3


def start_game(get_question_and_answer):
    name = welcome_user()
    for _ in range(NUM_OF_ROUNDS):
        question, answer = get_question_and_answer()
        print(f'Question: {question}')
        user_answer = prompt.string('Your answer: ')
        if user_answer == answer:
            print('Correct!')
        else:
            print(
                f"'{user_answer}' is wrong answer ;(. "
                f"Correct answer was '{answer}'."
            )
            print(f"Let's try again, {name}!")
            return
    else:
        print(f'Congratulations, {name}!')
