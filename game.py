import math
import random

# Base class for a player in the game (Human or Computer)
class Player:
    def __init__(self, letter):
        # 'letter' is X or O to represent the player
        self.letter = letter

    # Method to get the player's move, meant to be overridden by subclasses
    def get_move(self, game):
        pass


# A computer player that makes random moves
class RandomComputerPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)  # Initialize with X or O

    # Chooses a random move from the available moves
    def get_move(self, game):
        square = random.choice(game.available_moves())
        return square


# A human player that inputs moves manually
class HumanPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)  # Initialize with X or O

    # Gets a valid move from the user, keeps asking until valid input is provided
    def get_move(self, game):
        valid_square = False  # Tracks if the move is valid
        val = None
        while not valid_square:
            # Prompt user to input a square (0-8)
            square = input(self.letter + "'s turn. Input move (0-8): ")
            try:
                val = int(square)  # Try to convert the input into an integer
                # If move is not available, raise a ValueError
                if val not in game.available_moves():
                    raise ValueError
                valid_square = True  # If valid, exit the loop
            except ValueError:
                print('Invalid square. Try again.')  # Handle invalid input

        return val  # Return the valid move


# The Tic-Tac-Toe game class
class TicTacToe:
    def __init__(self):
        # Create a 3x3 board represented as a list of 9 spaces (' ')
        self.board = [' ' for _ in range(9)]
        self.current_winner = None  # Track the winner

    # Prints the current state of the board
    def print_board(self):
        # Divide the list into rows and print each row
        for row in [self.board[i * 3:(i + 1) * 3] for i in range(3)]:
            print('|' + '|'.join(row) + '|')

    @staticmethod
    def print_board_nums():
        # Prints a numbered board (for reference) so players know where to move
        number_board = [[str(i) for i in range(j * 3, (j + 1) * 3)] for j in range(3)]
        for row in number_board:
            print('|' + '|'.join(row) + '|')

    # Returns the available moves as a list of indices (empty spaces)
    def available_moves(self):
        return [i for i, spot in enumerate(self.board) if spot == ' ']

    # Checks if there are empty squares remaining on the board
    def empty_squares(self):
        return ' ' in self.board

    # Returns the number of empty squares remaining
    def num_empty_squares(self):
        return self.board.count(' ')

    # Makes a move on the board, placing the player's letter on a given square
    def make_move(self, square, letter):
        if self.board[square] == ' ':
            self.board[square] = letter  # Place the letter on the board
            # Check if the move wins the game
            if self.winner(square, letter):
                self.current_winner = letter  # Set the current winner
            return True
        return False  # Return False if the move is invalid

    # Determines if the current move results in a win
    def winner(self, square, letter):
        # Check the row for a win
        row_ind = square // 3  # Get the row index
        row = self.board[row_ind * 3:(row_ind + 1) * 3]  # Extract the row
        if all([spot == letter for spot in row]):
            return True

        # Check the column for a win
        col_ind = square % 3  # Get the column index
        column = [self.board[col_ind + i * 3] for i in range(3)]  # Extract the column
        if all([spot == letter for spot in column]):
            return True

        # Check diagonals for a win (only if the move was made on an even index)
        if square % 2 == 0:
            # Left to right diagonal
            diagonal1 = [self.board[i] for i in [0, 4, 8]]
            if all([spot == letter for spot in diagonal1]):
                return True
            # Right to left diagonal
            diagonal2 = [self.board[i] for i in [2, 4, 6]]
            if all([spot == letter for spot in diagonal2]):
                return True

        return False  # No win found


# Function to handle playing the game
def play(game, x_player, o_player, print_game=True):
    if print_game:
        game.print_board_nums()  # Print the numbered board for reference

    letter = 'X'  # Starting letter
    while game.empty_squares():  # Keep playing while there are empty squares
        # Get the move for the current player
        if letter == 'O':
            square = o_player.get_move(game)  # O player's turn
        else:
            square = x_player.get_move(game)  # X player's turn

        # Make the move
        if game.make_move(square, letter):
            if print_game:
                print(letter + f' makes a move to square {square}')
                game.print_board()  # Print the updated board
                print('')

            if game.current_winner:
                if print_game:
                    print(letter + ' wins!')  # Announce the winner
                return letter  # End the game and return the winner

            # Switch turns by alternating the letter (X -> O or O -> X)
            letter = 'O' if letter == 'X' else 'X'

    if print_game:
        print("It's a tie!")  # Announce a tie if no winner


# Main execution when the file is run directly
if __name__ == '__main__':
    x_player = HumanPlayer('X')  # X player is human
    o_player = RandomComputerPlayer('O')  # O player is computer
    t = TicTacToe()  # Create a TicTacToe game instance
    play(t, x_player, o_player, print_game=True)  # Start the game
