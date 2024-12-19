#!/usr/bin/env python3
from brain_games.engine import start_game
from brain_games.games.calc import get_expression_and_result


def main():
    start_game(get_expression_and_result)


if __name__ == '__main__':
    main()
