class CommandBuilder:

    def __init__(self, commands):
        self.commands = commands
    
    def is_unknown(self):
        if self.get_command_word() == " ":
            return True

    def get_word(self, index):
        return self.commands[index]

    def get_command_word(self):
        return self.commands[0]

    def get_command_words(self):
        return self.commands
    
    def get_command_length(self):
        return len(self.commands)