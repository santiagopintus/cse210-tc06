from game.board import Board
from game.console import Console
from game.guess import Guess
from game.player import Player
from game.roster import Roster

class Director:
    """A code template for a person who directs the game. The responsibility of 
    this class of objects is to control the sequence of play.
    
    Stereotype:
        Controller

    Attributes:
        board (Board): An instance of the class of objects known as Board.
        console (Console): An instance of the class of objects known as Console.
        guess (Guess): Current player's guess to be compared and stored.
        roster (Roster): An instance of the class of objects known as Roster.
        keep_playing (boolean): Whether or not the game can continue.
        code_length (int): The amount of digits of the code
        turn_count (int): (Optional) checks turn count, could be of use if adding more players
        winner (string): Gets the winner's name
    """

    def __init__(self):
        """The class constructor.
        
        Args:
            self (Director): an instance of Director.
        """
        self._board = Board()
        self._console = Console()
        self._guess = Guess()
        self._roster = Roster()
        self._keep_playing = True
        self._code_length = 4
        self._winner = ''
        self._turn_count = 0
        
    def start_game(self):
        """Starts the game loop to control the sequence of play.
        
        Args:
            self (Director): an instance of Director.
        """
        self._prepare_game()
        while self._keep_playing:
            self._get_inputs()
            self._do_updates()
            self._do_outputs()

    def _prepare_game(self):
        """Prepares the game before it begins. In this case, that means getting the player 
           names, adding them to the roster, and storing their assigned code, guess, and hint.
        
        Args:
            self (Director): An instance of Director.
        """
        green = '\033[92m'
        blue = '\033[94m'
        end_color = '\033[0m'
        current_color = green

        for n in range(2):
            #Setting the color of each player
            if current_color == green:
                current_color = blue
            else:
                current_color = green

            name = self._console.read(f"Enter a name for player {n + 1}: ")
            player = Player(f'{current_color}{name}{end_color}')
            self._roster.add_player(player)
            self._board.prepare()

    def _get_inputs(self):
        """Gets the inputs at the beginning of each round of play. In this case,
        that means getting the move from the current player.

        Args:
            self (Director): An instance of Director.
        """
        #start of turn, for optional use only
        self._add_turn_count()

        # display the game board
        board = self._board.display_board(self._roster)
        self._console.write(board)

        # get current player's guess
        player = self._roster.get_current()
        self._console.write(f"{player.get_name()}'s turn:")
        guess = self._console.ask_guess(self._code_length)
        self._guess.set_guess(guess)

    def _do_updates(self):
        """Updates the important game information for each round of play. In 
        this case, that means updating the board with the current move.

        Args:
            self (Director): An instance of Director.
        """
        # get current player details
        player = self._roster.get_current()
        players = self._roster.get_roster()

        # check winning condition, stop the game if player guessed right
        # if there's no win, store input and continue with the next player
        current_player_index = players.index(player)
        current_player_items = self._board._get_player_items(current_player_index)
        if current_player_items[0] == self._guess.get_guess():
            self._winner = player.get_name()
        else:
            code = current_player_items[0]
            guess = self._guess.get_guess()
            hint = self._board._create_hint(code, guess)
            self._board._set_player_items(current_player_index, guess, hint)
            
    def _do_outputs(self):
        """Outputs the important game information for each round of play. In 
        this case, that means checking if there are stones left and declaring the winner.

        Args:
            self (Director): An instance of Director.
        """
        if self._winner:
            print(f"\n{self._winner} won!")
            self._keep_playing = False
        self._roster.next_player()

    def _add_turn_count(self):
        """Proceeds to the next turn. Optional

        Args:
            self (Director): An instance of Director.
        """
        self._turn_count += 1
    
       