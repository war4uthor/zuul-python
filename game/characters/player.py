from characters.character import Character

class Player(Character):
    def __init__(self, name, items, max_weight):
        Character.__init__(self, name, items)
        self.max_weight = max_weight
    
    def get_max_weight(self):
        return self.max_weight

    def set_max_weight(self, max_weight):
        self.max_weight = max_weight