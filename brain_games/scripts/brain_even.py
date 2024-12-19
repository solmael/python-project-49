#!/usr/bin/env python3
from brain_games.engine import start_game
from brain_games.games.even import get_num_and_answer


def main():
    start_game(get_num_and_answer)


if __name__ == '__main__':
    main()
