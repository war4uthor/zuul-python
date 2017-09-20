from characters.player import Player
from commands.command import Command

class ItemsCommand(Command):
    def __init__(self, info, description):
        Command.__init__(self, info, description)
    
    def execute(self, game, command):
        player = game.get_player()
        inventory_string = " "
        if len(player.get_item_string()) == 0:
            inventory_string = "empty"
        else: 
            inventory_string = player.get_item_string()

        print("\nPlayer: %s\nWeight: %s\nInventory: %s\n" % (player.get_name(), player.get_weight(), inventory_string))

    def usage(self):
        return "Usage: items"