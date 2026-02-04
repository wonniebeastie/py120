import random
class Card:
    RANK_NUMBERS = {"Jack": 11, "Queen": 12, "King": 13, "Ace": 14}

    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def __str__(self):
        return f"{self.rank} of {self.suit}"

    @property
    def value(self):
        return Card.RANK_NUMBERS.get(self.rank, self.rank)

    def __lt__(self, other):
        return self.value < other.value

    def __eq__(self, other):
        return self.rank == other.rank and self.suit == other.suit

class Deck:

    RANKS = list(range(2, 11)) + ['Jack', 'Queen', 'King', 'Ace']
    # [2, 3, 4, 5, 6, 7, 8, 9, 10, 'Jack', 'Queen', 'King', 'Ace']
    SUITS = ['Hearts', 'Clubs', 'Diamonds', 'Spades']

    def __init__(self):
        self.reset_deck()

    def reset_deck(self):
        self.deck = self.create_deck()
        random.shuffle(self.deck)

    def create_deck(self):
        self.deck = []
        
        for rank in Deck.RANKS:
            for suit in Deck.SUITS:
                self.deck.append(Card(rank, suit))
        
        return self.deck

    def draw(self):
        if self.deck == []:
            self.reset_deck()
        return self.deck.pop()

# Test code
deck = Deck()
drawn = []
for _ in range(52):
    drawn.append(deck.draw())

count_rank_5 = sum([1 for card in drawn if card.rank == 5])
count_hearts = sum([1 for card in drawn if card.suit == 'Hearts'])

print(count_rank_5 == 4)      # True
print(count_hearts == 13)     # True

drawn2 = []
for _ in range(52):
    drawn2.append(deck.draw())

print(drawn != drawn2)        # True (Almost always).
