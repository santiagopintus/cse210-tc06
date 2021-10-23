import random
from game.roster import Roster
from game.player import Player

class Board:
    """The board that contains the game elements.
    
    Stereotype: 
        Information Holder

    Attributes:
        _player_items (list): A list of the players' assigned code, guess, and hint.
    """
    
    def __init__(self):
        """The class constructor.
        
        Args:
            self (Board): an instance of Board.
        """   
        self._player_items = []

    def prepare(self):
        """Sets up the board with an entry for the current player.
        
        Args:
            self (Board): an instance of Board.
        """
        code = str(random.randint(1000, 10000))
        guess = "----"
        hint = "****"
        self._player_items.append([code, guess, hint])
        
    def _create_hint(self, code, guess):
        """Generates a hint based on the given code and guess.

        Args:
            self (Board): An instance of Board.
            code (string): The code to compare with.
            guess (string): The guess that was made.

        Returns:
            string: A hint in the form [xxxx]
        """ 
        hint = ""
        for index, letter in enumerate(guess):
            if code[index] == letter:
                hint += "x"
            elif letter in code:
                hint += "o"
            else:
                hint += "*"
        return hint

    def _set_player_items(self, player_index, guess, hint):
        """Sets the current player's guess and hint.

        Args:
            self (Board): An instance of Board.
            guess (string): The guess that was made.
            hint (string): The hint that's given based on the guess.
        """ 
        self._player_items[player_index][1] = guess
        self._player_items[player_index][2] = hint

    def _get_player_items(self, player_index):
        """Gets the current player's code, guess, and hint

        Args:
            self (Board): An instance of Board.
            player_index (int): Player's place in the roster.
        
        Returns: 
            list: Current player's stored details
        """ 
        return self._player_items[player_index]

    def display_board(self, roster):
        """Displays the current board in string format

        Args:
            self (Board): An instance of Board.
            roster (Roster): Roster of all players.
        
        Returns: 
            string: The board in string format.
        """ 
        board_string = '\n--------------------' 
        players = roster.get_roster()
        for player in players:
            index = players.index(player)
            guess = self._player_items[index][1]
            hint = self._player_items[index][2]
            board_string += (f"\nPlayer {player.get_name()}: {guess}, {hint}")  
        board_string += '\n--------------------\n'
        return board_string
        



    