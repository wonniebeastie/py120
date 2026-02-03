"""
[x] Add a end of the game message function - add a space
[x] change loop in `play()` to work with `for` loop instead (extract to 
   `play_turn`)
[x] separate the 3 jobs that `evaluate_guess` is doing rn
    [x] returns guess int
    [x] prints feedback to user
    [x] mutates `self.guesses_remaining`
"""
# For computing the number of guesses:
import math
import random

class GuessingGame:

    def __init__(self, low, high):
        self.secret_number = None
        self.max_guesses = int(math.log2(high - low + 1)) + 1
        self.guesses_remaining = range(self.max_guesses, 0, -1)
        self.number_range = range(low, high + 1)

    def reset(self):
        self.secret_number = random.choice(self.number_range)

    def get_guess(self):
        while True:
            guess = input(f"Enter a number between {self.number_range[0]} and {self.number_range[-1]}: ")
            if guess.isdigit():
                guess = int(guess)
                if guess in self.number_range:
                    return guess
            print("Invalid guess. ", end="")

    def display_guesses_remaining(self, remaining):
        print()
        if remaining == 1:
            print("You have 1 guess remaining.")
        else:
            print(f"You have {remaining} guesses remaining.")

    def evaluate_guess(self, guess):
        if guess < self.secret_number:
            return "low"
        elif guess > self.secret_number:
            return "high"
        else:
            return "match"

    def display_status_message(self, status):
        match status:
            case "low":
                print("Your number is too low.")
            case "high":
                print("Your number is too high.")
            case "match":
                print("That's the number!")

    def play_turn(self):
        for remaining_guesses in self.guesses_remaining:
            print(f"remaining_guesses: {remaining_guesses}")
            self.display_guesses_remaining(remaining_guesses)
            guess = self.get_guess()
            guess_status = self.evaluate_guess(guess)
            self.display_status_message(guess_status)

            if guess_status == "match":
                return "win"
            
            # self.guesses_remaining -= 1

        return "lose"

    def display_end_message(self, result):
        if result == 'win':
            print("\n", "You won!")
        else:
            print("\n","You have no more guesses. You lost!")

    def play(self):
        self.reset()
        print(self.secret_number) #TODO: REMOVE !!!!!
        game_result = self.play_turn()
        print(f"game_result: {game_result}")
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
