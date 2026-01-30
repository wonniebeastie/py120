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
"""
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
