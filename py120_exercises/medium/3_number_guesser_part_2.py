"""
[x] Update Solution:
    [x] accept a low & high value when `GuessingGame` objects are initialized
    [x] use the values to compute a `secret_number` for the game.

[] Change number of guesses allowed
    - so user can always win if she uses a good strategy.
"""
# For computing the number of guesses:
import math
import random

class GuessingGame:
    MAX_GUESSES = 7

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
                    return self.evaluate_guess(guess)
            print("Invalid guess. ", end="")

    def play_turn(self):
        print()
        if self.guesses_remaining == 1:
            print("You have 1 guess remaining.")
        else:
            print(f"You have {self.guesses_remaining} guesses remaining.")
        return self.get_guess()

    def play(self):
        self.reset()
        print(self.secret_number)
        while self.guesses_remaining > 0:
            if self.play_turn():
                print("You won!")
                return
        
        print("You have no more guesses. You lost!")

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
