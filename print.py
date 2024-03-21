import random

def print_players(players):
    print('The following players are still in the game:')
    for player in players:
        print(player.name)


def print_players_visitedPlaces_and_FavWeapons(player1, player2):
    player1_places = random.choice(player1.visited_places)
    player2_places = random.choice(player2.visited_places)
    player1_weapon = random.choice(player1.fav_weapons)
    player2_weapon = random.choice(player2.fav_weapons)
    print(f"Player {player1.name} visited places: {player1_places} and his favotite weapon is: {player1_weapon} ")
    print(f"Player {player2.name} visited places: {player2_places} and his favotite weapon is: {player2_weapon} ")