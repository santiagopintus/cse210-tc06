class Guess:
    """The player's guess.
    
    Stereotype: 
        Information Holder

    Attributes:
        guess (string): The player's guess
    """
    def __init__(self):
        """The class constructor.
        
        Args:
            self (Guess): an instance of Guess.
        """  
        self.__guess = ''

    def set_guess(self, guess):
        """Sets the player's guess for storage.

        Args:
            self (Board): An instance of Board.
            guess (string): The player's guess
        """ 
        self.__guess = guess

    def get_guess(self):
        """Gets the current player's guess.

        Args:
            self (Guess): An instance of Guess.
        
        Returns: 
            string: The current player's guess.
        """ 
        return self.__guess 