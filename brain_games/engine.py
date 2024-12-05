import prompt
from brain_games.const import NUM_OF_ROUNDS


def start_game(get_question_and_answer, INSTRUCTION):
    name = prompt.string('Welcome to the Brain Games!\n'
                         'May I have your name? ')
    print(f'Hello, {name}!\n'
          f'{INSTRUCTION}')
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
            return False
    print(f'Congratulations, {name}!')
