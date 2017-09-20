from commands.command_builder import CommandBuilder

class Parser:
    def __init__(self, game):
        self.game = game
    
    def parse_command(self):
        command = input("> ")
        #Split command by whitespace
        command_words = command.split()

        return CommandBuilder(command_words)