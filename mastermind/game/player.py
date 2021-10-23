class Player:
    """A person taking part in a game. The responsibility of Player is to keep track of their identity and last move.
    
    Stereotype: 
        Information Holder

    Attributes:
        _name (string): The player's name.
        _move (Move): The player's last move.
    """
    def __init__(self, name):
        """The class constructor.
        
        Args:
            self (Player): an instance of Player.
        """
        self._name = name

    def get_name(self):
        """Returns the player's name.

        Args:
            self (Player): an instance of Player.
        """
        return self._name