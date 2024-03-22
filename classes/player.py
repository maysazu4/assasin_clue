class player:
    def __init__(self,name,visited_places = [],fav_weapons = []):
        self.name = name
        self.visited_places = visited_places
        self.fav_weapons = fav_weapons
        self.is_murderer = False
       