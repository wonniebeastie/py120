"""
Rules:
    - a random number is generated at the beginning of the game
    - 7 guesses per game
    - each "turn" looped until either:
        - player runs out of guesses
        - guesses correctly and wins
    - if player guesses wrongly, display whether the guess was too low or too high
    - a game object should start a NEW game with a NEW number to guess with each
    call to `play`
    - class should be called `GuessingGame`

Flow:
    1) random number is generated (hidden)
    2) display number of guesses remaining
    3) ask player to input a number b/w 1 ~ 100 (inclusive)
        => guess is invalid:
            - display that the guess is invalid, and ask to enter again
        => guess is valid:
            - player guesses wrong:
                - display whether the guess is too high or too low
                - decrement number of guesses by 1
                - loop back to #2
            - player guesses correctly:
                - display "That's the number!"
                - display that they won
                - end game

`GuessingGame` Responsibilities:
    - start a new game each time (`play()`)
    - run the game loop (repeat turns until win/loss)
    - get and validate input (must be b/w 1-100; re-prompt for invalid)
    - give feedback/output (too high/low, guesses remaining, win/lose messages)

Pieces of State `GuessingGame` Will Need:
    Persistant: 
        - max number of guesses 
        - number range boundary 1-100 (`SECRET_NUM_RANGE`)
    Per-Game:
        - `secret_number`
        - `guesses_remaining`

What is "one turn"?:
    - display guesses remaining
    - prompt until a valid guess (1-100)
    - compare to secret number -> print feedback (low/high/correct)
    - if valid & incorrect, decrement number of guesses

Methods:
- `play()` -> play one full game
    - call `reset()`
    - while `guesses_remaining` is greater than 0:
        - do one turn
        - if turn results in a correct guess (`play_turn` returns True):
            - print win message & end `play()`
    - if loop ends (guesses ran out) -> end with loss message

- `reset()` -> resets per-game state
    - new `secret_number`
    - `guesses_remaining` = 7

- `play_turn()` -> handles one guess attempt
    O: boolean
    - display `guesses_remaining`
    - return `get_guess()`

- `get_guess(self)` -> gets a valid guess from player
    O: boolean
    - while True:
        - SET `guess` with input from player
        - check if `guess` is an integer and is within `SECRET_NUM_RANGE`:
            - if it is:
                - break out of loop
            - else:
                - print "Invalid guess" -> loop back `print(msg, end='')`
    - return `evaluate_guess(self, guess)`

- `evaluate_guess(self, guess)` -> 
    I: int, guess
    O: boolean
    - compare `guess` with `secret_number`
    - if `guess` is:
        - less than `secret_number`:
            - print "Your guess is too low."
            - decrement `guesses_remaining`
            - return False
        - greater than `secret_number`:
            - print "Your guess is too high."
            - decrement `guesses_remaining`
            - return False
        - correct:
            - print "That's the number!"
            - return True
"""
import random
class GuessingGame:
    MAX_GUESSES = 7
    SECRET_NUM_RANGE = range(1, 100 + 1)

    def __init__(self):
        self.secret_number = None
        self.guesses_remaining = 0

    def reset(self):
        self.secret_number = random.choice(GuessingGame.SECRET_NUM_RANGE)
        self.guesses_remaining = 7

    def evaluate_guess(self):
        pass

    def get_guess(self):
        pass

    def play_turn(self):
        pass

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

# game.play()

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
