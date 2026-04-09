import random

class Square:
    INITIAL_MARKER = " "
    HUMAN_MARKER = "X"
    COMPUTER_MARKER = "O"

    def __init__(self, marker=INITIAL_MARKER):
        self.marker = marker

    @property
    def marker(self):
        return self._marker

    @marker.setter
    def marker(self, marker):
        self._marker = marker

    def __str__(self):
        return self.marker

    def is_unused(self):
        return self.marker == Square.INITIAL_MARKER

class Board:
    def __init__(self):
        self.squares = {key: Square() for key in range(1, 10)}

    def display(self):
        print()
        print("     |     |")
        print(f"  {self.squares[1]}  |"
              f"  {self.squares[2]}  |"
              f"  {self.squares[3]}")
        print("     |     |")
        print("-----+-----+-----")
        print("     |     |")
        print(f"  {self.squares[4]}  |"
              f"  {self.squares[5]}  |"
              f"  {self.squares[6]}")
        print("     |     |")
        print("-----+-----+-----")
        print("     |     |")
        print(f"  {self.squares[7]}  |"
              f"  {self.squares[8]}  |"
              f"  {self.squares[9]}")
        print("     |     |")
        print()

    def mark_square_at(self, key, marker):
        self.squares[key].marker = marker

    def unused_squares(self):
        return [key
                for key, square in self.squares.items()
                if square.is_unused()]

class Row:
    def __init__(self):
        # STUB
        # We need some way to identify a row of 3 squares
        pass

class Player:
    def __init__(self, marker):
        # STUB
        # A player is either a human or a computer that is
        #   playing the game.
        # Perhaps we need a "marker" to keep track of this
        #   player's symbol? (i.e., 'X' or 'O')
        self.marker = marker

    @property
    def marker(self):
        return self._marker

    @marker.setter
    def marker(self, value):
        self._marker = value

class Human(Player):
    def __init__(self):
        # STUB
        # What does a human player need to do? How does it
        #   differ from the basic Player or a Computer?
        super().__init__(Square.HUMAN_MARKER)

class Computer(Player):
    def __init__(self):
        # STUB
        # What does a computer player need to do? How does
        #   it differ from the basic Player or a Human?
        super().__init__(Square.COMPUTER_MARKER)

class TTTGame:
    def __init__(self):
        self.board = Board()
        self.human = Human()
        self.computer = Computer()

    def play(self):
        # SPIKE
        self.display_welcome_message()

        while True:
            self.board.display()

            self.human_moves()
            if self.is_game_over():
                break

            self.computer_moves()
            if self.is_game_over():
                break

        self.board.display()
        self.display_results()
        self.display_goodbye_message()

    def display_welcome_message(self):
        print("Welcome to Tic Tac Toe!")

    def display_goodbye_message(self):
        print("Thanks for playing Tic Tac Toe! Goodbye!")

    def display_results(self):
        # STUB
        # Show the results of this game (win, lose, tie)
        pass

    def human_moves(self):
        choice = None
        valid_choices = self.board.unused_squares()
        choices_list = [str(choice) for choice in valid_choices]
        choices_str = ", ".join(choices_list)

        while True:
            prompt =f"Choose a square({choices_str}): "
            choice = input(prompt)

            try:
                choice = int(choice)
                if choice in valid_choices:
                    break
            except ValueError:
                pass

            print("Sorry, that's not a valid choice.")
            print()

        # Mark the chosen square with the human's marker.
        self.board.mark_square_at(choice, self.human.marker)

    def computer_moves(self):
        valid_choices = self.board.unused_squares()
        choice = random.choice(valid_choices)
        self.board.mark_square_at(choice, self.computer.marker)

    def is_game_over(self):
        return self.board_is_full() or self.someone_won()

    def board_is_full(self):
        unused_squares = self.board.unused_squares()
        return len(unused_squares) == 0

    def someone_won(self):
        # STUB
        return False

game = TTTGame()
game.play()
