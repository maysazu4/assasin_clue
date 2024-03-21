from file_handler.load_file import *



def get_places(file):
    parsed_object  = load_file(file) 
    places = []
    for place in parsed_object['places']:
        places.append(place)
    return places


    