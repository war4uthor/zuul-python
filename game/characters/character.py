import random

class Character:
    def __init__(self, name, items):
        self.name = name
        self.items = items
        self.weight = 0
    
    def get_name(self):
        return self.name

    def move(self):
        exits = []
        for exit in self.get_room().get_exits():
            if self.get_room().get_exits()[exit] is not None:
                exits.append(exit)

        random_direction = random.choice(list(exits))

        self.get_room().remove_character(self)
        self.set_room(self.get_room().get_exit(random_direction))
        self.get_room().add_character(self)

    def set_name(self, name):
        self.name = name

    def get_items(self):
        return self.items
    
    def get_item_string(self):
        item_string = ""
        for item in self.items:
            item_string += "[" + item.get_name() + ", " + str(item.get_weight()) + "]" + ", "
        item_string = item_string.strip(", ")
        return item_string

    def get_item(self, item_name):
        return next((item for item in self.items if item.name == item_name), None)

    def set_items(self, items):
        self.items = items

    def get_room(self):
        return self.room

    def set_room(self, room):
        self.room = room

    def pickup_item(self, item_name):
        self.items.append(item_name)

    def drop_item(self, item_name):
        for item in self.items:
            if item.get_name() == item_name:
                self.items.remove(item)
    
    def get_weight(self):
        return self.weight

    def set_weight(self):
        self.weight = 0
        for item in self.items:
            self.weight += item.get_weight()
        
