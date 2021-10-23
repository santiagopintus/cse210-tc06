class Console:
    """A code template for a computer console. The responsibility of this 
    class of objects is to get text or numerical input and display text output.
    
    Stereotype:
        Service Provider, Interfacer

    Attributes:
        prompt (string): The prompt to display on each line.
    """
     
    def read(self, prompt):
        """Gets text input from the user through the screen.

        Args: 
            self (Screen): An instance of Screen.
            prompt (string): The prompt to display to the user.

        Returns:
            string: The user's input as text.
        """
        return input(prompt)

    def read_number(self, prompt):
        """Gets numerical input from the user through the screen.

        Args: 
            self (Screen): An instance of Screen.
            prompt (string): The prompt to display to the user.

        Returns:
            integer: The user's input as an integer.
        """
        return int(input(prompt))
        
    def write(self, text):
        """Displays the given text on the screen. 

        Args: 
            self (Screen): An instance of Screen.
            text (string): The text to display.
        """
        print(text)

    def ask_guess(self, code_lenght):
        """Asks and validates the guess received from the user

        Args: 
            self (Screen): An instance of Screen.
            code_lenght (number): The number of characters allowed

        Returns:
            string: The guess validated
        """
        invalid_guess = True

        while invalid_guess:
            guess = input("What is your guess? ")

            if guess.isnumeric():
                if len(guess) == code_lenght:
                    # If there is no error
                    invalid_guess = False
                    return guess
                else:
                    #Error 2: Guess is more than the code_lenght
                    self.write_error(f'Your guess needs to have {code_lenght} digits')
            else:
                #Error 1: The guess contains letters
                self.write_error('Your guess needs to be numeric')

    def write_error(self, text):
        """Displays the given error on the screen. 

        Args: 
            self (Screen): An instance of Screen.
            text (string): The error to display.
        """
        print(f'\033[1;31;40m{text}\033[0;37;40m')