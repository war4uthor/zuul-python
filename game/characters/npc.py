from characters.character import Character

class Npc(Character):
    def __init__(self, name, items, description):
        Character.__init__(self, name, items)
        self.description = description
    
    def get_description(self):
        return self.description

    def set_description(self, description):
        self.description = description
        