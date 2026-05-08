import random

class Card:
    SUITS = ('Hearts', 'Diamonds', 'Clubs', 'Spades')
    RANKS = ('Ace', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'Jack', 'Queen', 'King')

    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __repr__(self):
        return f'{self.rank} of {self.suit}'

class Deck:
    def __init__(self):
        self.cards = []
        for suit in Card.SUITS:
            for rank in Card.RANKS:
                self.cards.append(Card(suit, rank))
        random.shuffle(self.cards)

    def draw(self):
        return self.cards.pop()

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
        self.deck = Deck()

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
        # Use a helper to do the initial dealing of 2 cards to each participant
        # helper: deck.draw()
        self.deck.draw()

    def show_cards(self):
        # STUB
        # show each participants' hands
        # TODO: hide one of dealer's
        pass

    def player_turn(self):
        # STUB
        pass

    def dealer_turn(self):
        # STUB
        pass

    def display_welcome_message(self):
        print("Welcome to a game of Twenty-One. Let's play!")

    def display_goodbye_message(self):
        print("Thanks for playing Twenty-One. Goodbye.")

    def display_result(self):
        # STUB
        pass

game = TwentyOneGame()
game.start()

# test
deck = Deck()
print(deck.cards)
print(len(deck.cards))
