from commands.command import Command

class HelpCommand(Command):
    def __init__(self, info, description):
        Command.__init__(self, info, description)
        
    def execute(self, game, command):
        command_list = game.get_command_handler().get_commands_list()


        print("\nYour list of commands:\n")
        for k in command_list:
            print(k + ": " + command_list[k].get_description() + " " + command_list[k].usage())
        print("\n")
        
    def usage(self):
        return "Usage: help"
