from characters.player import Player
from commands.command import Command

class GoCommand(Command):
    def __init__(self, info, description):
        Command.__init__(self, info, description)
        
    def execute(self, game, command):
        if command.get_command_length() > 1:
            player = game.get_player()
            if player.get_room().get_exit(command.get_word(1)) is not None:

                characters = game.character_handler.get_characters()

                for character in characters:
                    if type(character) is not Player:
                        character.move()
                
                player.get_room().remove_character(player)
                player.set_room(player.get_room().get_exit(command.get_word(1)))
                player.get_room().add_character(player)
                print(player.get_room().get_long_description())

            else:
                #No exits
                print("\nYou cannot go that way!")
                #Print possible exits
                print(player.get_room().get_exit_string() + "\n")
        else:
            print("\nGo where?\n")

    def usage(self):
        return "Usage: go [direction]"