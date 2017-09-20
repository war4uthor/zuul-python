from commands.command import Command

class GiveCommand(Command):
    def __init__(self, info, description):
        Command.__init__(self, info, description)
        
    def execute(self, game, command):
        if command.get_command_length() > 2:
            player = game.get_player()
            item = player.get_item(command.get_word(1))
            character = player.get_room().get_character(command.get_word(2))
            if character is not None and item is not None:
                player.drop_item(item.get_name())
                player.set_weight()
                character.pickup_item(item)
                character.set_weight()
                print("\nYou give the %s to %s.\n" % (command.get_word(1), command.get_word(2)))
            elif character is None:
                print("\n`%s' is not in the room.\n" % command.get_word(2))
                return
            elif item is None:
                print("\nYou are not carrying a `%s'.\n" % command.get_word(1))
                return
        elif command.get_command_length() == 1:
            print("\nGive %s to who?\n" % command[1].get_name())
        else:
            print("\nGive what to who?\n")
        
    def usage(self):
        return "Usage: give [item] [character]"
