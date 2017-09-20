from commands.command import Command

class DropCommand(Command):
    def __init__(self, info, description):
        Command.__init__(self, info, description)
        
    def execute(self, game, command):
        player = game.get_player()

        if command.get_command_length() > 1 and player.get_item(command.get_word(1)) is not None:
            player.get_room().add_item(player.get_item(command.get_word(1)))
            player.drop_item(command.get_word(1))
            player.set_weight()
            print("\nYou drop the %s in the %s.\n" % (command.get_word(1), player.get_room().get_name().lower()))
        else:
            print("\nDrop what?\n")
        
    def usage(self):
        return "Usage: drop [item]"
