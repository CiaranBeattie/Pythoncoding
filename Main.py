import random
import math


# Base class for any player in the Tic-Tac-Toe game
class Player:
    def __init__(self, letter):
        # The player will be assigned either 'X' or 'O'
        self.letter = letter

    # Method to be implemented by subclasses for getting the player's move
    def get_move(self, game):
        pass


# Class for a computer player that selects a move at random
class RandomComputerPlayer(Player):
    def __init__(self, letter):
        # Initialize the RandomComputerPlayer with 'X' or 'O' using the parent class
        super().__init__(letter)

    # Override the get_move method to make a random move
    def get_move(self, game):
        # Choose a random move from the available moves on the game board
        square = random.choice(game.available_moves())
        return square


# Class for a human player that inputs their move manually
class HumanPlayer(Player):
    def __init__(self, letter):
        # Initialize the HumanPlayer with 'X' or 'O' using the parent class
        super().__init__(letter)

    # Override the get_move method to prompt the human for input
    def get_move(self, game):
        valid_square = False  # Boolean to keep track if the input is valid
        val = None  # Variable to store the validated move
        while not valid_square:
            # Prompt the human player to input a number (0-8) for their move
            square = input(self.letter + "'s turn. Input move (0-8): ")
            try:
                # Try to convert the input to an integer
                val = int(square)
                # Check if the chosen square is available on the game board
                if val not in game.available_moves():
                    raise ValueError  # Raise an error if the square is not valid
                valid_square = True  # If valid, exit the loop
            except ValueError:
                # If the input was invalid, print an error message and retry
                print('Invalid square. Try again.')

        return val  # Return the valid move
