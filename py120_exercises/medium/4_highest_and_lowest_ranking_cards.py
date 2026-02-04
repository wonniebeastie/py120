"""
Rules:
- numeric cards == low cards (2-10)
- jacks are higher than 10s
- queens higher than jacks
- kings higher than queens
- aces higher than kings
- suit plays no part in ranking
- if 2 or more cards of same rank in list:
    - min & max methods should return one of them, doesn't matter which
- update class so that built in `min()` & `max()` functions work on list of
  `Card` objects
- investigate magic methods & `__lt__` in particular.

Methods:
- any needed to determine lowest & highest
[x] custom `__str__` method:
    - returns a str representation of the card like "Jack of Diamonds"
      or "4 of Clubs", etc.

Brainstorm:
- assign numbers to each card to determine rank
    - since numeric cards already have a number, just assign a number to
      the non-numeric cards (dictionary, class constant)
        - Jack: 11
        - Queen: 12
        - King: 13
        - Ace: 14
    - use those numbers to determine rank
- `min()` & `max()` need to treat the cards as their numbers, but no direct way
  to compare custom objects.
"""
# Update this class to determine lowest & highest ranking cards in a list of
# `Card` objects:
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

# Test code
cards = [Card(2, 'Hearts'),
         Card(10, 'Diamonds'),
         Card('Ace', 'Clubs')]
print(min(cards) == Card(2, 'Hearts'))             # True
print(max(cards) == Card('Ace', 'Clubs'))          # True
print(str(min(cards)) == "2 of Hearts")            # True
print(str(max(cards)) == "Ace of Clubs")           # True

cards = [Card(5, 'Hearts')]
print(min(cards) == Card(5, 'Hearts'))             # True
print(max(cards) == Card(5, 'Hearts'))             # True
print(str(Card(5, 'Hearts')) == "5 of Hearts")     # True

cards = [Card(4, 'Hearts'),
         Card(4, 'Diamonds'),
         Card(10, 'Clubs')]
# print(min(cards).rank == 4)                        # True
# print(max(cards) == Card(10, 'Clubs'))             # True
print(str(Card(10, 'Clubs')) == "10 of Clubs")     # True

cards = [Card(7, 'Diamonds'),
         Card('Jack', 'Diamonds'),
         Card('Jack', 'Spades')]
print(min(cards) == Card(7, 'Diamonds'))           # True
print(max(cards).rank == 'Jack')                   # True
print(str(Card(7, 'Diamonds')) == "7 of Diamonds") # True

cards = [Card(8, 'Diamonds'),
         Card(8, 'Clubs'),
         Card(8, 'Spades')]
print(min(cards).rank == 8)                        # True
print(max(cards).rank == 8)                        # True
