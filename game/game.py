from room.room import Room
from item.item import Item
from characters.npc import Npc
from characters.player import Player
from handlers.itemhandler import ItemHandler
from handlers.characterhandler import CharacterHandler
from handlers.roomhandler import RoomHandler
from handlers.commandhandler import CommandHandler
from parser.parser import Parser

class Game:
    
    finished = False

    def __init__(self):
        self.play()
    
    def setup(self):
        #Setup commands
        self.command_handler = CommandHandler()

        #Setup items
        self.item_handler = ItemHandler()
        self.item_handler.setup()
        
        #Setup characters
        self.character_handler = CharacterHandler(self.item_handler, self.player_name)
        self.character_handler.setup()
        
        #Setup rooms
        self.room_handler = RoomHandler(self.item_handler, self.character_handler)
        self.room_handler.setup()

        self.parser = Parser(self)
    
    def play(self):
        self.player_name = input("\nEnter your name: ")
        self.setup()
        self.print_welcome()
        while self.finished == False:
            command = self.parser.parse_command()
            self.process_command(command)
        return

    def get_player(self):
        return self.character_handler.get_player()

    def process_command(self, command):

        if command.is_unknown() or self.command_handler.get_command(command.get_command_word()) is None:
            print("\nCommand not recognised. Type 'help' to see a list of available commands.\n")
        else:
            self.command_handler.get_command(command.get_command_word()).execute(self, command)
    
    def get_command_handler(self):
        return self.command_handler

    def print_welcome(self):
        print("\nWelcome %s, to World of Zuul: Python edition!\nType 'help' if you need help." % self.player_name)
        print(self.get_player().get_room().get_long_description())
    
    def print_quit_message(self):
        print("\nThank you for playing World of Zuul: Python edition!\n\nWritten by J.L.G. McBride, Autumn 2017.\n")

        
    
        
        
