
from launch_game import *


def main():
    players,places = set_up_game()
    launch_game(players, places)


if __name__ == '__main__':
    main()