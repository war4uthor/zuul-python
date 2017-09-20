class Room:
    def __init__(self, name, description, exits, characters, items):
        self.name = name
        self.description = description
        self.exits = exits
        self.characters = characters
        self.items = items
    
    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def get_description(self):
        return self.description

    def set_description(self, description):
        self.description = description
    
    def get_exit(self, direction):
        if direction in self.exits:
            return self.exits[direction]
        else:
            return None

    def get_exits(self):
        return self.exits

    def set_exits(self, exits):
        self.exits = exits
    
    def get_exit_string(self):
        exit_string = "Exits: " 
        for exit in self.exits:
            if self.exits.get(exit) is not None:
                exit_string += exit + ", "
        exit_string = exit_string.strip(", ")
        return exit_string

    def get_character_string(self):
        character_string = "Characters: "
        for character in self.characters:
            character_string += character.get_name() + ", "
        character_string = character_string.strip(", ")
        return character_string
    
    def get_item_string(self):
        item_string = "Items: "
        for item in self.items:
            item_string += "[" + item.get_name() + ", " + str(item.get_weight()) + "]" + ", "
        item_string = item_string.strip(", ")
        return item_string

    def get_long_description(self):
        return "\nYou are in %s\n\n%s\n%s\n%s\n" % (self.get_description(), self.get_exit_string(), self.get_character_string(), self.get_item_string())

    def get_character(self, name):
        return next((character for character in self.characters if character.name == name), None)
    
    def get_characters(self):
        return self.characters

    def set_characters(self, characters):
        self.characters = characters
        for character in self.characters:
            character.set_room(self)

    def get_items(self):
        return self.items

    def get_item(self, item_name):
        return next((item for item in self.items if item.name == item_name), None)

    def set_items(self, items):
        self.items = items

    def add_item(self, item):
        self.items.append(item)
    
    def remove_item(self, item):
        if item in self.items: self.items.remove(item)

    def add_character(self, character):
        self.characters.append(character)
    
    def remove_character(self, character):
        self.characters.remove(character)