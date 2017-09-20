from characters.character import Character
from characters.player import Player
from characters.npc import Npc

class CharacterHandler:
    
    characters = []

    def __init__(self, item_handler, player_name):
        self.item_handler = item_handler
        self.player_name = player_name
    
    def setup(self):
        #Create characters
        lumberjack = Npc("Bob", [self.item_handler.get_item("apple")], "A friendly lumberjack")
        princess = Npc("Rapunzel", [], "A beautiful princess with long blonde hair")
        caveman = Npc("Rocky", [], "A caveman with a big bushy beard")
        witch = Npc("Morgana", [self.item_handler.get_item("wand"), self.item_handler.get_item("toad")], "A wicked witch dressed in black")
        bard = Npc("Lofty", [self.item_handler.get_item("lyre")], "A whimsical bard playing a lyre")
        king = Npc("James", [self.item_handler.get_item("crown")], "The benevolent king of the land")
        player = Player(self.player_name, [], 20)

        self.characters.append(player)
        self.characters.append(lumberjack)
        self.characters.append(princess)
        self.characters.append(caveman)
        self.characters.append(witch)
        self.characters.append(bard)
        self.characters.append(king)
        
    def get_characters(self):
        return self.characters

    def get_character(self, name):
        for character in self.characters: 
            if character.name == name:
                return character
            
    def get_player(self):
        return next((character for character in self.characters if character.name == self.player_name))