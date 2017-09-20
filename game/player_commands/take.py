from commands.command import Command

class TakeCommand(Command):
    def __init__(self, info, description):
        Command.__init__(self, info, description)
        
    def execute(self, game, command):
        
        player = game.get_player()

        if command.get_command_length() > 1:
            if player.get_room().get_item(command.get_word(1)) is not None:
                if player.get_weight() + player.get_room().get_item(command.get_word(1)).get_weight() <= player.get_max_weight():
                    player.pickup_item(player.get_room().get_item(command.get_word(1)))
                    player.set_weight()
                    player.get_room().remove_item(player.get_room().get_item(command.get_word(1)))
                    print("\nYou pick up the %s in the %s.\n" % (command.get_word(1), player.get_room().get_name().lower()))
                else:
                    print("\n%s is too heavy!\n" % (player.get_room().get_item(command[1]).get_name()))
            else:
                print("\n%s not found in the %s.\n" % (command.get_word(1), player.get_room().get_name().lower()))
        else:
            print("\nTake what?\n")

    def usage(self):
        return "Usage: take [item]"