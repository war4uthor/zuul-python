from commands.command import Command

class QuitCommand(Command):
    def __init__(self, info, description):
        Command.__init__(self, info, description)
        
    def execute(self, game, command):
        game.print_quit_message()
        game.finished = True
    
    def usage(self):
        return "Usage: quit"
