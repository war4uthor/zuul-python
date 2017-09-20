from characters.player import Player
from commands.command import Command

class InspectCommand(Command):
    def __init__(self, info, description):
        Command.__init__(self, info, description)

    def execute(self, game, command):
        player = game.get_player()

        if command.get_command_length() > 1:
            if type(player.get_room().get_character(command.get_word(1))) is Player:
                print("\nYou can't inspect yourself!\n")
                return
            if player.get_room().get_character(command.get_word(1)) is not None:
                character = player.get_room().get_character(command.get_word(1))
                
                inventory_string = " "
                
                if len(character.get_item_string()) == 0:
                    inventory_string = "nothing"
                else: 
                    inventory_string = character.get_item_string()
    
                print("\n%s: %s. Carrying: %s\n" % (character.get_name(), character.get_description(), inventory_string))
            
            elif player.get_room().get_item(command.get_word(1)) is not None:
                
                item = player.get_room().get_item(command.get_word(1))
                print("\n%s: %s, weight: %s\n" % (item.get_name(), item.get_description(), item.get_weight()))

            elif player.get_item(command.get_word(1)) is not None:
                item = player.get_item(command.get_word(1))
                print("\n%s: %s, weight: %s\n" % (item.get_name(), item.get_description(), item.get_weight()))
            else:
                print("\nInspect what?\n")
        else:
                print("\nInspect what?\n")
                
            

    def usage(self):
        return "Usage: inspect [item]/[character]"