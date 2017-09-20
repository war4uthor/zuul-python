from room.room import Room
from item.item import Item
from characters.character import Character
from handlers.characterhandler import CharacterHandler


class RoomHandler:
    
    rooms = []

    def __init__(self, item_handler, character_handler):
        self.characters = character_handler
        self.items = item_handler
    
    def setup(self):
        #Create rooms
        forest = Room("Forest", "an enchanted forest. You hear a gentle breeze whistling through its trees.", {}, [self.characters.get_character("Bob"), self.characters.get_character("Lofty")],[])
        tower = Room("Tower", "a tall stone tower elevated above the clouds.", {}, [self.characters.get_character("Rapunzel")], [self.items.get_item("hairbrush")])
        cave = Room("Cave", "a deep, rocky cavern. Voices are emanating from deep within.", {}, [self.characters.get_character("Rocky")], [self.items.get_item("lantern"), self.items.get_item("book")])
        cottage = Room("Cottage", "a quaint little cottage with a thatched roof. A thick, green smog fumes from the chimney.", {}, [self.characters.get_character("Morgana")], [self.items.get_item("broomstick")])
        swamp = Room("Swamp", "a dark, murky swamp. The marshes bubble and ooze slime.", {}, [self.characters.get_player()], [self.items.get_item("watch")])
        castle = Room("Castle", "an enormous castle with a moat and drawbridge. Its lofty spires are adorned with gold.",{}, [self.characters.get_character("James")],[self.items.get_item("gold")])

        #Create exits
        forest.set_exits({"north" : cave, "east" : tower, "south" : castle, "west" : None})
        tower.set_exits({"north" : cottage, "east" : None, "south" : swamp, "west" : forest})
        cave.set_exits({"north" : None, "east" : cottage, "south" : forest, "west" : None})
        cottage.set_exits({"north" : None, "east" : None, "south" : tower, "west" : cave})
        swamp.set_exits({"north" : tower, "east" : None, "south" : None, "west" : castle})
        castle.set_exits({"north" : forest, "east" : swamp, "south" : None, "west" : None})

        self.characters.get_player().set_room(swamp)
        self.characters.get_character("Bob").set_room(forest)
        self.characters.get_character("Lofty").set_room(forest)
        self.characters.get_character("Rapunzel").set_room(tower)
        self.characters.get_character("Rocky").set_room(cave)
        self.characters.get_character("Morgana").set_room(cottage)
        self.characters.get_character("James").set_room(castle)

    def get_rooms(self):
        return self.rooms

    def get_room(self, name):
        for room in self.rooms: 
            if room.name == name:
                return room
    
    def get_character_handler(self):
        return self.characters