from print import *
import random
import classes.player as p
from file_handler.get_places import *
from file_handler.get_weapons import *
import time as t

class PlayerNotFoundError(Exception):
        pass
weapons_num_min = 1
weapons_num_max = 3

'''
Find a common visited place between the murderer and the victim
parameters : victim - a player who was randomly selected to be a victim
             murderer - the murderer player
returns : common place if found, None else
'''
def choose_common_visited_place(victim, murderer):
    for place in victim.visited_places:
        if place in murderer.visited_places:
            return place
    return None


'''
Selects the murder victim randomly, and the place from the visited places by the murderer ,
 and the weapon from his favourite weapons
parameters : murderer - a player object
             players - list of player objects, has all the players in the game
returns : the murder victim, place, weapon
'''
def murder(murderer,players):
    killed = False
    while(killed == False):
        # choose the victim randomly
        victim = random.choice(players)
        if victim == murderer:
            continue
        # choose the murder place from the murderer visited places
        place = choose_common_visited_place(victim, murderer)
        if place == None:
            continue
        # choose the murder weapon from the murderer favourite weapons
        weapon = random.choice(murderer.fav_weapons)
        killed = True
    if killed == False:
        return None,None
    return victim,place,weapon


'''
Get a list of places and number of places, select places_num places from the
 list and returns a list of the selected places
parameters: places - list of strings, each string is a name of a place
            places_num - integer, which is a number between 1 to 3, describes the number of places to select
returns: visited - a list of places
'''
def choose_places(places , places_num):
    visited = []
    while(places_num !=0):
        place= random.choice(places)
        if place not in visited:
            places_num -= 1
            visited.append(place)   
    return visited


'''
Gets a list of players and update the visited places of each player to 1 - 3 places from the places list
parameters: players - a list of all the players in the game 
            places - a list of all the places in the game
returns : None , update the field visited_places for each player
'''
def visit(players , places):
    for player in players:
        places_num = random.randint(1, 3)
        player.visited_places = choose_places(places , places_num)  
        if player.is_murderer == True:
            visited_places = player.visited_places
    # To gurentee that at least one player has a common vistited place with the murderer, to avoid infinite loop
    for player in players:
        if player.is_murderer == False:
            player.visited_places.pop()
            place = random.choice(visited_places)
            player.visited_places.append(place)
            break
    for player in players:
        print(f"player {player.name} visited the following places {player.visited_places}")  


'''
Gets a list of players and selects one randomly to be the murderer
parameters: players - a list of player object 
returns: murderer - a player object is selected from the list
'''
def pick_murderer(players):
    if not players or players == []:
        raise ValueError("Player list is empty.")
    murderer = random.choice(players)
    if not isinstance(players,list) :
        raise TypeError("Input must be a list of player objects.")
    if not isinstance(murderer,p.player):
        raise ValueError("Input must be a list of player objects.")

    murderer.is_murderer = True
    return murderer
    


''' 
Gets  players name and list of players and returns the player with this name as a player object
parameters: players - a list of player objects, 
            name - a string
returns: player - player object who has the given name 
         None - if there is no player with the given name
'''    
def get_player_by_name(players,name):
    for player in players:
        if player.name == name:
            return player
    return None
'''
Ask the user to choose 2 players whom he suspects, and retruns them

Parameters:
players(list): list that contains objects of type "player"

Returns:
player1,player2(player):two players of type player
'''        
def suspect(players):
    try:
        if not isinstance(players,list):
            raise ValueError("Input must be a list of player objects.")
        print_players(players)
        players_input = input("Please choose two players whom you suspect (separated by a space): ")
        # Split the input based on the space delimiter
        suspected = players_input.split()
        # Ensure that exactly two players were entered
        while len(suspected) != 2:
            players_input = input("Please enter exactly two players separated by a space.")
            suspected = players_input.split() 
        player1 = get_player_by_name(players,int(suspected[0]))
        player2 = get_player_by_name(players,int(suspected[1]))
        if player1 is None or player2 is None:
            raise PlayerNotFoundError("Player not found")  
        return player1,player2
    except TypeError as te:
        print("Error,suspect:", te)
    except PlayerNotFoundError as pne:
        print("Error:", pne)
    except Exception as e:
        print("Error suspect:", e)
     
    
'''
Gets two players, and asks the user to pick one of them to accuse
parameters: player1,player2 - player objects
returns: the name of the player the user selects
'''
def accuse(player1, player2):
    try:
        if not isinstance(player1,p.player) or not isinstance(player2,p.player) :
            raise ValueError("Input must be a player objects.")
        accused = int(input('Please choose the player you want to accuse: '))
        while accused != player1.name and accused != player2.name:
            accused = int(input('Please make sure to choose a player from the list of suspects you provided earlier: '))
        return accused
    except TypeError as te:
        print("Error:", te)
    except Exception as e:
        print("Error:", e)
    

'''
Runs a round, a murder happen, and then try to guss the murderer
parameters: players - a list of player objects
            places - list of strings, all the places in the game
            murderer - a player object , the murderer of the game
returns: True - if the player guesses the murderer 
         False - otherwise
'''
def round(players,places,murderer):
    print('\n New Round Started\n')
    # each player visits between 1 to 3 places
    visit(players,places)
    # a murder occured
    victim,place,weapon = murder(murderer,players)
    # while victim == None :
    #     victim,place,weopon = murder(murderer,players)
    players.remove(victim)
    print('\n')
    print(f" *** Player {victim.name} was killed in {place} using {weapon}. *** ")
    t.sleep(1.0)
    print('\n')
    print('......')
    if len(players) == 1:
            return False
    player1 , player2 = suspect(players) 
    print_players_visitedPlaces_and_FavWeapons(player1, player2)
    accused = accuse(player1, player2)
    if accused == murderer.name:
        return True
    return False


'''
The main game function, picks a murderer and each round perform a murder, and lets the user guess who is the murderer
if he succeds the game ends and the user wins,else the game continues to another round,
if the murderer is the only player remains in the game the game ends and the murderer wins
parameters: players - a list of player objects
            places - list of strings, all the places in the game
returns: None
'''
def launch_game(players,places):
    murderer = pick_murderer(players)
    print(murderer.name)
    success = False
    while(success != True):
        if len(players) == 1:
            print(f"\nGame Over, the murderer {murderer.name} win")
            break
        success = round(players,places,murderer)
        if success:
            print('\nCongratulations! Your accusation is correct. You have found the murderer')
            break
        else:
            print('\nSorry, your accusation is incorrect. You have not found the murderer this time')


'''
    Set up the game by assigning random favorite weapons to each player,
    and load the data of places and weapons from the files

    returns:
        players (list): A list of player objects.
        places (list): A list of strings , each one is a name of a place.
'''

def set_up_game():
    places = get_places('user_data\\places.json')
    weapons = get_weapons('user_data\\weapons.json')
    players_num = int(input('please enter the number of players: '))
    players = [p.player(i) for i in range(players_num)]
    for player in players:
        weapons_num = random.randint(weapons_num_min, weapons_num_max)
        player.fav_weapons = choose_places(weapons , weapons_num)   
    return players,places   



