import random
class Card:
    """
    Produce a single card & allow for comparison
    """
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
    """
    Produce a deck of cards & allow for drawing of 1 card
    """
    RANKS = list(range(2, 11)) + ['Jack', 'Queen', 'King', 'Ace']
    SUITS = ['Hearts', 'Clubs', 'Diamonds', 'Spades']

    def __init__(self):
        self._reset()

    def _reset(self):
        self._deck = self.create_deck()
        random.shuffle(self._deck)

    def create_deck(self):
        self._deck = [Card(rank, suit)
                      for rank in Deck.RANKS
                      for suit in Deck.SUITS]
        
        return self._deck

    def draw(self):
        if self._deck == []:
            self._reset()
        return self._deck.pop()

# Include Card and Deck classes from the last two exercises.
# Some variants of Poker allow both Ace-high (A, K, Q, J, 10) and 
# Ace-low (A, 2, 3, 4, 5) straights. 
# For simplicity, your code only needs to recognize Ace-high straights.
class PokerHand:
    """
    Takes 5 cards from a `Deck` of `Cards` & evaluates those cards as a poker
    hand.
    """
    def __init__(self, deck):
        pass

    def print(self):
       pass

    def evaluate(self):
        if self._is_royal_flush():
            return "Royal flush"
        elif self._is_straight_flush():
            return "Straight flush"
        elif self._is_four_of_a_kind():
            return "Four of a kind"
        elif self._is_full_house():
            return "Full house"
        elif self._is_flush():
            return "Flush"
        elif self._is_straight():
            return "Straight"
        elif self._is_three_of_a_kind():
            return "Three of a kind"
        elif self._is_two_pair():
            return "Two pair"
        elif self._is_pair():
            return "Pair"
        else:
          return "High card"

    def _is_royal_flush(self):
        """
        # 1
        MOST POWERFUL
        Highest 5 cards in the same suit
        (A K Q J 10) - all diamonds
        """
        pass

    def _is_straight_flush(self):
        """
        # 2
        5 cards in consecutive order of the same suit
        8 7 6 5 4 - all spades
        """
        pass

    def _is_four_of_a_kind(self):
        """
        # 3
        4 cards of the same rank & one different kind ("kicker")
        JH JD JS JC 7D
        """
        pass

    def _is_full_house(self):
        """
        # 4
        3 cards of the same rank & 2 cards of another rank
        10H 10D 10C 9S 9D
        """
        pass

    def _is_flush(self):
        """
        # 5
        Any 5 cards in the same suit not in sequence
        4 J 8 2 9 (suits are not involved)
        """
        pass

    def _is_straight(self):
        """
        # 6
        5 consecutive cards but with different suits
        Highest: A K Q J 10
        Lowest: 5 4 3 2 A ("wheel")
        """
        pass

    def _is_three_of_a_kind(self):
        """
        # 7
        3 cards of the same rank & 2 unrelated cards
        7S 7D 7C KC 3D 
        """
        pass

    def _is_two_pair(self):
        """
        # 8
        2 cards with same rank in pairs & a different kind ("kicker")
        4S 4C 3S 3D QS
        """
        pass

    def _is_pair(self):
        """
        # 9
        2 cards of same rank & 3 independent cards
        AH AD 8S 4C 7H
        """
        pass

# Test code
hand = PokerHand(Deck())
hand.print()
print(hand.evaluate())
print()

# Adding TestDeck class for testing purposes

class TestDeck(Deck):
    def __init__(self, cards):
        self._deck = cards

# All of these tests should return True

hand = PokerHand(
    TestDeck(
        [
            Card("Ace", "Hearts"),
            Card("Queen", "Hearts"),
            Card("King", "Hearts"),
            Card("Jack", "Hearts"),
            Card(10, "Hearts"),
        ]
    )
)
print(hand.evaluate() == "Royal flush")

hand = PokerHand(
    TestDeck(
        [
            Card(8, "Clubs"),
            Card(9, "Clubs"),
            Card("Queen", "Clubs"),
            Card(10, "Clubs"),
            Card("Jack", "Clubs"),
        ]
    )
)
print(hand.evaluate() == "Straight flush")

hand = PokerHand(
    TestDeck(
        [
            Card(3, "Hearts"),
            Card(3, "Clubs"),
            Card(5, "Diamonds"),
            Card(3, "Spades"),
            Card(3, "Diamonds"),
        ]
    )
)
print(hand.evaluate() == "Four of a kind")

hand = PokerHand(
    TestDeck(
        [
            Card(3, "Hearts"),
            Card(3, "Clubs"),
            Card(5, "Diamonds"),
            Card(3, "Spades"),
            Card(5, "Hearts"),
        ]
    )
)
print(hand.evaluate() == "Full house")

hand = PokerHand(
    TestDeck(
        [
            Card(10, "Hearts"),
            Card("Ace", "Hearts"),
            Card(2, "Hearts"),
            Card("King", "Hearts"),
            Card(3, "Hearts"),
        ]
    )
)
print(hand.evaluate() == "Flush")

hand = PokerHand(
    TestDeck(
        [
            Card(8, "Clubs"),
            Card(9, "Diamonds"),
            Card(10, "Clubs"),
            Card(7, "Hearts"),
            Card("Jack", "Clubs"),
        ]
    )
)
print(hand.evaluate() == "Straight")

hand = PokerHand(
    TestDeck(
        [
            Card("Queen", "Clubs"),
            Card("King", "Diamonds"),
            Card(10, "Clubs"),
            Card("Ace", "Hearts"),
            Card("Jack", "Clubs"),
        ]
    )
)
print(hand.evaluate() == "Straight")

hand = PokerHand(
    TestDeck(
        [
            Card(3, "Hearts"),
            Card(3, "Clubs"),
            Card(5, "Diamonds"),
            Card(3, "Spades"),
            Card(6, "Diamonds"),
        ]
    )
)
print(hand.evaluate() == "Three of a kind")

hand = PokerHand(
    TestDeck(
        [
            Card(9, "Hearts"),
            Card(9, "Clubs"),
            Card(5, "Diamonds"),
            Card(8, "Spades"),
            Card(5, "Hearts"),
        ]
    )
)
print(hand.evaluate() == "Two pair")

hand = PokerHand(
    TestDeck(
        [
            Card(2, "Hearts"),
            Card(9, "Clubs"),
            Card(5, "Diamonds"),
            Card(9, "Spades"),
            Card(3, "Diamonds"),
        ]
    )
)
print(hand.evaluate() == "Pair")

hand = PokerHand(
    TestDeck(
        [
            Card(2, "Hearts"),
            Card("King", "Clubs"),
            Card(5, "Diamonds"),
            Card(9, "Spades"),
            Card(3, "Diamonds"),
        ]
    )
)
print(hand.evaluate() == "High card")
# Should output:
# NOTE: The exact cards and the type of hand for the first test will vary with 
# each run, so don't expect the same output we show for the first 6 lines.

# 5 of Clubs
# 7 of Diamonds
# Ace of Hearts
# 7 of Clubs
# 5 of Spades
# Two pair

# true
# true
# true
# true
# true
# true
# true
# true
# true
# true
# true
# true
# true
