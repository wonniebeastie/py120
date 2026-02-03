"""
[x] Add a end of the game message function - add a space
[x] change loop in `play()` to work with `for` loop instead (extract to 
   `play_turn`)
[] separate the 3 jobs that `evaluate_guess` is doing rn
    [] returns true/false
    [] prints feedback to user
    [] mutates `self.guesses_remaining`
"""
# For computing the number of guesses:
import math
import random

class GuessingGame:

    def __init__(self, low, high):
        self.secret_number = None
        self.guesses_remaining = 0
        self.low = low
        self.high = high
        self.number_range = range(self.low, self.high + 1)

    def reset(self):
        self.secret_number = random.choice(self.number_range)
        self.guesses_remaining = int(math.log2(self.high - self.low + 1)) + 1

    def evaluate_guess(self, guess):
        if guess < self.secret_number:
            print("Your number is too low.")
            self.guesses_remaining -= 1
            return False
        elif guess > self.secret_number:
            print("Your number is too high.")
            self.guesses_remaining -= 1
            return False
        else:
            print("That's the number!")
            return True

    def get_guess(self):
        while True:
            guess = input(f"Enter a number between {self.low} and {self.high}: ")
            if guess.isdigit():
                guess = int(guess)
                if guess in self.number_range:
                    return guess
            print("Invalid guess. ", end="")

    def display_guessses_remaining(self):
        print()
        if self.guesses_remaining == 1:
            print("You have 1 guess remaining.")
        else:
            print(f"You have {self.guesses_remaining} guesses remaining.")

    # change 
    def play_turn(self):
        for guess_number in self.guesses_remaining:
            self.display_guessses_remaining()
            # get_guess
            # guess_status = evaluate_guess()
            # display low/high/match
            # result = 
        # return game result

    def display_end_message(result):
        if result == 'win':
            print("\n", "You won!")
        else:
            print("\n","You have no more guesses. You lost!")

    def play(self):
        self.reset()
        print(self.secret_number) #TODO: REMOVE !!!!!
        game_result = play_turn()
        self.display_end_message(game_result)

game = GuessingGame(501, 1500)
game.play()

# You have 10 guesses remaining.
# Enter a number between 501 and 1500: 104
# Invalid guess. Enter a number between 501 and 1500: 1000
# Your guess is too low.

# You have 9 guesses remaining.
# Enter a number between 501 and 1500: 1250
# Your guess is too low.

# You have 8 guesses remaining.
# Enter a number between 501 and 1500: 1375
# Your guess is too high.

# You have 7 guesses remaining.
# Enter a number between 501 and 1500: 80
# Invalid guess. Enter a number between 501 and 1500: 1312
# Your guess is too low.

# You have 6 guesses remaining.
# Enter a number between 501 and 1500: 1343
# Your guess is too low.

# You have 5 guesses remaining.
# Enter a number between 501 and 1500: 1359
# Your guess is too high.

# You have 4 guesses remaining.
# Enter a number between 501 and 1500: 1351
# Your guess is too low.

# You have 3 guesses remaining.
# Enter a number between 501 and 1500: 1355
# That's the number!

# You won!

game.play()
# You have 10 guesses remaining.
# Enter a number between 501 and 1500: 1000
# Your guess is too high.

# You have 9 guesses remaining.
# Enter a number between 501 and 1500: 750
# Your guess is too low.

# You have 8 guesses remaining.
# Enter a number between 501 and 1500: 875
# Your guess is too high.

# You have 7 guesses remaining.
# Enter a number between 501 and 1500: 812
# Your guess is too low.

# You have 6 guesses remaining.
# Enter a number between 501 and 1500: 843
# Your guess is too high.

# You have 5 guesses remaining.
# Enter a number between 501 and 1500: 820
# Your guess is too low.

# You have 4 guesses remaining.
# Enter a number between 501 and 1500: 830
# Your guess is too low.

# You have 3 guesses remaining.
# Enter a number between 501 and 1500: 835
# Your guess is too low.

# You have 2 guesses remaining.
# Enter a number between 501 and 1500: 836
# Your guess is too low.

# You have 1 guess remaining.
# Enter a number between 501 and 1500: 837
# Your guess is too low.

# You have no more guesses. You lost!
