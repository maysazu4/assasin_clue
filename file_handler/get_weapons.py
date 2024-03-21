from file_handler.load_file import *



def get_weapons(file):
    parsed_object  = load_file(file) 
    weapons = []
    for weapon in parsed_object['weapons']:
        weapons.append(weapon)
    return weapons


    