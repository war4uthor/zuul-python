from commands.command import Command

class LookCommand(Command):
    def __init__(self, info, description):
        Command.__init__(self, info, description)
        
    def execute(self, game, command):
        print(game.get_player().get_room().get_long_description())


    def usage(self):
        return "Usage: look"