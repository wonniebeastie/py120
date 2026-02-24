import random
class Player:
    CHOICES = ('rock', 'paper', 'scissors')

    def __init__(self, player_type):
        # maybe a "name"?
        self._player_type = player_type.lower()
        self.move = None

    def _is_human(self):
        return self._player_type == 'human'

    def choose(self):
        if self._is_human():
            # choose human player's move
        else:
            self.move = random.choice(Player.CHOICES)

class Move:
    def __init__(self):
        # This seems like we need something to keep track
        # of the choice... a move object can be "paper", "rock" or "scissors"
        pass

class Rule:
    def __init__(self):
        # not sure what the "state" of a rule object should be
        pass

    # not sure where "compare" goes yet
    def compare(self, move1, move2):
        pass

class RPSGame:
    def __init__(self):
        self._human = Player('human')
        self._computer = Player('computer')

    def _display_welcome_message(self):
        print('Welcome to Rock Paper Scissors!')

    def _display_goodbye_message(self):
        print('Thanks for playing Rock Paper Scissors. Goodbye!')

    def play(self):
        self._display_welcome_message()
        self._human.choose()
        self._computer.choose()
        display_winner()
        self._display_goodbye_message()
