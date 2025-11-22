###############################
# Tic Tac Toe Game
###############################

import random
import os

class TicTacToe():
    
    def __init__(self):
        self.p1 = input(f"Please enter your name: ")
        self.p2 = input(f"Please enter your name: ")
        self.game_board = [
            ['  ', '1', ' ', '2', ' ', '3',],
            ['a ', ' ', '|', ' ', '|', ' ',],
            ['  ', '-', '-', '-', '-', '-',],
            ['b ', ' ', '|', ' ', '|', ' ',],
            ['  ', '-', '-', '-', '-', '-',],
            ['c ', ' ', '|', ' ', '|', ' ']
        ]
        self.score = {self.p1: 0, self.p2: 0}
        self.positions = {
            'a1': '', 'a2': '', 'a3': '',
            'b1': '', 'b2': '', 'b3': '',
            'c1': '', 'c2': '', 'c3': '',
        }

    def clear_screen(self):
        """Clear the console for readability"""
        os.system('cls' if os.name == 'nt' else 'clear')

    def display_board(self):
        """Display board status"""
        # Show current state of board
        for row in self.game_board:
            print(''.join(row))

    def update_board(self, position, piece):
        """Update board and position tracker with player moves"""        
        # Map positions to game_board
        position_map = {
            'a1': (1, 1), 'a2': (1, 3), 'a3': (1, 5),
            'b1': (3, 1), 'b2': (3, 3), 'b3': (3, 5),
            'c1': (5, 1), 'c2': (5, 3), 'c3': (5, 5)
        }

        # Check if valid move or already played
        # Update self.positions. Update self.game_board
        if position in position_map and self.positions[position] == '':
            self.positions[position] = piece
            row, col = position_map[position]
            self.game_board[row][col] = piece
            return True
        
        # Else return False
        return False

    def check_result(self, piece):
        """Check if the piece completes a line."""
        # All possible winning combinations
        wins = [
            ['a1', 'a2', 'a3'], ['b1', 'b2', 'b3'], ['c1', 'c2', 'c3'],  # rows
            ['a1', 'b1', 'c1'], ['a2', 'b2', 'c2'], ['a3', 'b3', 'c3'],  # cols
            ['a1', 'b2', 'c3'], ['a3', 'b2', 'c1']   # diagonals
        ]

        # Check if there is a complete line
        for line in wins:
            if all(self.positions[pos] == piece for pos in line):
                return True
        return False

    def check_board_full(self):
        """Check if the board is full"""        
        # Check if the board is full
        return all(value != '' for value in self.positions.values())

    def new_game(self):
        """Reset boards ready for new Game"""
        self.game_board = [
            ['  ', '1', ' ', '2', ' ', '3',],
            ['a ', ' ', '|', ' ', '|', ' ',],
            ['  ', '-', '-', '-', '-', '-',],
            ['b ', ' ', '|', ' ', '|', ' ',],
            ['  ', '-', '-', '-', '-', '-',],
            ['c ', ' ', '|', ' ', '|', ' ']
        ]
        self.positions = {
            'a1': '', 'a2': '', 'a3': '',
            'b1': '', 'b2': '', 'b3': '',
            'c1': '', 'c2': '', 'c3': '',
        }
        self.game()

    def game(self):
        # Play game
        x_or_o = ['X', 'O']
        random.shuffle(x_or_o)
        players = {self.p1: x_or_o[0], self.p2: x_or_o[1]}

        print(f"\n{self.p1} is '{x_or_o[0]}'.")
        print(f"{self.p2} is '{x_or_o[1]}'\n")

        current_player = random.choice([self.p1, self.p2])
        print(f"{current_player} will go first.\n")

        while True:
            self.display_board()
            piece = players[current_player]

            # Move
            move = input(f"\n{current_player}, please enter your move, (a1-c3): ").lower().strip()

            if move not in self.positions:
                print("Invalid position! Use format like 'a1', 'b2'.")
                continue

            # Player goes
            if self.update_board(move, piece):
                
                # Check if there is a winner
                if self.check_result(piece):
                    self.display_board()
                    print(f"{current_player} wins!")
                    self.score[current_player] += 1
                    break

                # Check if there is a tie
                if self.check_board_full():
                    self.display_board()
                    print("\nIt's a tie! Game Over.")
                    break

                # Switch players
                current_player = self.p2 if current_player == self.p1 else self.p1
            
            else:
                print("Invalid move! Try again.")                
        
        # Show score and see if they want to play again!
        print(f"\nCurrent score: {self.p1}: {self.score[self.p1]} | {self.p2}: {self.score[self.p2]}")       
        while True:
            play_again = input("Do you want to play again? Enter Y or N: ").lower()
            if play_again in ['y', 'n']:
                break
            print("Invalid input. Please enter Y or N.")

        if play_again == "y":
            self.new_game()

        if play_again == "n":
            print(f"\nFinal Score: {self.p1}: {self.score[self.p1]} | {self.p2}: {self.score[self.p2]}")
            print("Thanks for playing!\n")

if __name__ == "__main__":
    play = TicTacToe()
    play.game()
