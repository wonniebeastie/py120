import random
class GuessingGame:
    MAX_GUESSES = 7
    NUMBER_RANGE = range(1, 100 + 1)

    def __init__(self):
        self.secret_number = None
        self.guesses_remaining = 0

    def reset(self):
        self.secret_number = random.choice(GuessingGame.NUMBER_RANGE)
        self.guesses_remaining = 7

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
            guess = input("Enter a number between 1 and 100: ")
            if guess.isdigit():
                guess = int(guess)
                if guess in GuessingGame.NUMBER_RANGE:
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
        while self.guesses_remaining > 0:
            if self.play_turn():
                print("You won!")
                return
        
        print("You have no more guesses. You lost!")

game = GuessingGame()
game.play()

# You have 7 guesses remaining.
# Enter a number between 1 and 100: 104
# Invalid guess. Enter a number between 1 and 100: 50
# Your guess is too low.

# You have 6 guesses remaining.
# Enter a number between 1 and 100: 75
# Your guess is too low.

# You have 5 guesses remaining.
# Enter a number between 1 and 100: 85
# Your guess is too high.

# You have 4 guesses remaining.
# Enter a number between 1 and 100: 0
# Invalid guess. Enter a number between 1 and 100: 80
# Your guess is too low.

# You have 3 guesses remaining.
# Enter a number between 1 and 100: 81
# That's the number!

# You won!

game.play()

# You have 7 guesses remaining.
# Enter a number between 1 and 100: 50
# Your guess is too high.

# You have 6 guesses remaining.
# Enter a number between 1 and 100: 25
# Your guess is too low.

# You have 5 guesses remaining.
# Enter a number between 1 and 100: 37
# Your guess is too high.

# You have 4 guesses remaining.
# Enter a number between 1 and 100: 31
# Your guess is too low.

# You have 3 guesses remaining.
# Enter a number between 1 and 100: 34
# Your guess is too high.

# You have 2 guesses remaining.
# Enter a number between 1 and 100: 32
# Your guess is too low.

# You have 1 guess remaining.
# Enter a number between 1 and 100: 32
# Your guess is too low.

# You have no more guesses. You lost!
