from file_handler.get_places import *
from file_handler.get_weapons import *
from launch_game import *

weapons_num_min = 1
weapons_num_max = 3

def main():
    places = get_places('user_data\places.json')
    weapons = get_weapons('user_data\weapons.json')
    players_num = int(input('please enter the number of players: '))
    players = [p.player(i) for i in range(players_num)]
    for player in players:
        weapons_num = random.randint(weapons_num_min, weapons_num_max)
        player.fav_weapons = choose_places(weapons , weapons_num) 
    launch_game(players, places,weapons)
if __name__ == '__main__':
    main()