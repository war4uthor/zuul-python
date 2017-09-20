from item.item import Item
class ItemHandler:
    
    #List of items
    items = []

    def __init__(self):
        pass
    
    def setup(self):
        #Create items
        apple = Item("apple", "a shiny red apple", 3)
        book = Item("book", "a dusty old tome", 4)
        watch = Item("watch", "a silver wristwatch", 2)
        lantern = Item("lantern", "a burnt out lantern", 7)
        broomstick = Item("broomstick", "an old broom, imbued with magic", 9)
        wand = Item("wand", "a magic wand", 2)
        toad = Item("toad", "a slimy green toad", 4)
        lyre = Item("lyre", "a stringed musical instrument", 8)
        hairbrush = Item("hairbrush", "a prized belonging of the princess", 3)
        gold = Item("gold", "a large bag of gold coins", 10)
        crown = Item("crown", "the royal crown", 8)

        self.items.append(apple)
        self.items.append(book)
        self.items.append(watch)
        self.items.append(lantern)
        self.items.append(broomstick)
        self.items.append(wand)
        self.items.append(toad)
        self.items.append(lyre)
        self.items.append(hairbrush)
        self.items.append(gold)
        self.items.append(crown)

    def get_items(self):
        return self.items

    def get_item(self, name):
        return next((item for item in self.items if item.name == name), None)