class Card:
    def __init__(self):
        # STUB
        # A Card needs:
        # rank
        # suit
        # points? or compute from its rank
        pass

class Deck:
    def __init__(self):
        # STUB
        # A Deck needs:
        # a collection of 52 Cards
        pass

class Participant:
    def __init__(self):
        # STUB
        # Each participants needs:
        # a hand
        pass

    def hit(self):
        # STUB
        pass

    def stay(self):
        # STUB
        pass

    def is_busted(self):
        # STUB
        pass

    def score(self):
        # STUB
        pass

class Player(Participant):
    def __init__(self):
        # STUB
        # A player needs, in addition to the ones in Participant:
        # betting money (starts at $5)
        pass

class Dealer(Participant):
    def __init__(self):
        # STUB
        # Very similar to a Player; do we need this?
        pass

    def hide(self):
        # STUB
        pass

    def reveal(self):
        # STUB
        pass

class TwentyOneGame:
    def __init__(self):
        # STUB
        # A game needs:
        # a shuffled deck of cards
        # players
        pass

    def start(self):
        # SPIKE
        self.display_welcome_message()
        self.deal_cards()
        self.show_cards()
        self.player_turn()
        self.dealer_turn()
        self.display_result()
        self.display_goodbye_message()

    def deal_cards(self):
        # STUB
        pass

    def show_cards(self):
        # STUB
        pass

    def player_turn(self):
        # STUB
        pass

    def dealer_turn(self):
        # STUB
        pass

    def display_welcome_message(self):
        # STUB
        pass

    def display_goodbye_message(self):
        # STUB
        pass

    def display_result(self):
        # STUB
        pass

game = TwentyOneGame()
game.start()
