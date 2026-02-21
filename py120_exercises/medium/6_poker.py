import random
class Card:
    """
    FUNCTIONS:
    - produces a single card
    - prints how you'd call a card in English
    - allows for comparison of cards
    Ex:
    - an instance => Card("Ace", "Hearts")
    - print(card) => Ace of Hearts
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
    FUNCTIONS:
    - produces a new, shuffled 52-card deck of cards
    - allows for drawing of 1 card
    Ex:
    - an instance => Deck()
        - an internal list like [Card(...), Card(...), ...]
    - card1 = deck.draw() => "7 of Hearts" or "Ace of Spades"
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

    All methods for winning combos return a boolean.
    """
    def __init__(self, deck):
        self._cards = [deck.draw() for _ in range(5)]

    def print(self):
        for card in self._cards:
            print(card)

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
          return "High card" # The highest card in hand when no winning combos

    def check_consecutive(self, numeric_ranks):
        """
        Return true if the numbers in the list are consecutive, false otherwise
        I: a list, of ranks as integers
        O: boolean

        - for each number:
            - add 1 to that number
            - if that number is different to the the one that comes after the
              current number:
                - return False
        - return True
        """
        for idx in range(len(numeric_ranks) - 1):
            if numeric_ranks[idx] + 1 != numeric_ranks[idx + 1]:
                return False
        return True

    def check_suit(self, suits):
        """
        Checks if all suits are the same one.
        I: a list, of suits
        O: boolean

        - SET `first` with the first element of `suits`
        - return numeric_ranks of checking if `suits` & `first` are the same value
          using `all()`
        """
        first = suits[0]
        return all(suit == first for suit in suits)

    def compare_ranks(self, rank_count_match):
        """
        Checks if a sorted ranks list is the same as the hand we want
        I: a list, the match we want the ranks of a hand to be compared to
        O: boolean
        """
        all_ranks = self.get_ranks()
        rank_counts = list(self.count_ranks(all_ranks).values())
        rank_counts.sort()

        return rank_counts == rank_count_match

    def convert_to_numeric(self, ranks):
        """
        Convert all ranks to numeric value if not already numeric.
        I: a list, of ranks
        O: a list, of ranks but in their numeric form

        Ex:
        ['Jack', 10, 'Queen', 9, 8] => [11, 10, 12, 9, 8]

        - empty list
        - for rank in ranks:
            - if rank is a string:
                - get the value (number) of rank from `RANK_NUMBERS`
                - add it to empty list
            - else:
                - add it to empty list
        - return list
        """
        numeric_ranks = []
        for rank in ranks:
            if isinstance(rank, str):
                numeric_ranks.append(Card.RANK_NUMBERS[rank])
            else:
                numeric_ranks.append(rank)
        return numeric_ranks

    def count_ranks(self, all_ranks):
        """
        Create a frequency map of the ranks in a hand
        I: a list, of ranks
        O: a dict, counts
        """
        rank_counts = {}
        for rank in all_ranks:
            rank_counts[rank] = rank_counts.get(rank, 0) + 1

        return rank_counts

    def get_ranks(self):
        """
        Collect all ranks of a hand into a list & return it
        """
        return [card.rank for card in self._cards]

    def get_suits(self):
        """
        Collect all the suits of a hand into a list & return it
        """
        return [card.suit for card in self._cards]

    def _is_royal_flush(self):
        """
        # 1
        MOST POWERFUL
        Highest 5 cards in the same suit
        (A K Q J 10) - all diamonds
        """
        all_suits = self.get_suits()

        if self.check_suit(all_suits):
            all_ranks = self.get_ranks()
            highest_five = {"Ace", "Queen", "King", "Jack", 10}
            if set(all_ranks) == highest_five:
                return True
        return False

    def _is_straight_flush(self):
        """
        # 2
        5 cards in consecutive order of the same suit
        8 7 6 5 4 - all spades
        """
        """
        - SET `all_suits` with returning list from `get_suits()`
        - if `check_suit(all_suits)` returns true:
            - SET `all_ranks` with returning list from `get_ranks()`
            - SET `numeric_ranks` with returning list from 
              `convert_to_numeric(all_ranks)`
            - sort those values
            - check whether they form consecutive numbers: [TODO: extract to 
            another helper?]
                - if yes, return True
        - return False
        """
        all_suits = self.get_suits()

        if self.check_suit(all_suits):
            # TODO: Extract me from here?
            all_ranks = self.get_ranks()
            numeric_ranks = self.convert_to_numeric(all_ranks)
            numeric_ranks.sort()
            # TODO: to here (maybe)
            return self.check_consecutive(numeric_ranks)
        else:
            return False

    def _is_four_of_a_kind(self):
        """
        # 3
        4 cards of the same rank & one different kind ("kicker")
        JH JD JS JC 7D
        """
        """
        - SET `all_ranks` with ranks of all cards as a list
        - SET `unique_ranks` with a set version of `all_ranks`
        - for `rank` in `unique_ranks`:
            - count how many times that `rank` appears in `all_ranks`
            - if that `rank` appears 4 times:
                - return True
        - return False
        """
        all_ranks = self.get_ranks()
        unique_ranks = set(all_ranks)

        for rank in unique_ranks:
            rank_count = all_ranks.count(rank)
            if rank_count == 4:
                return True

        return False

    def _is_full_house(self):
        """
        # 4
        3 cards of the same rank & 2 cards of another rank
        10H 10D 10C 9S 9D
        """
        """
        - SET `all_ranks` with ranks of all cards as a list
        - SET `rank_counts` with a frequency count of all the ranks
        - look at the counts in `rank_counts`:
            - if there is a count of 3 AND a count of 2:
                - return True
        - return False
        """
        all_ranks = self.get_ranks()
        rank_counts = self.count_ranks(all_ranks)
        return 2 in rank_counts.values() and 3 in rank_counts.values()

    def _is_flush(self):
        """
        # 5
        Any 5 cards in the same suit not in sequence
        4C JC 8C 2C 9C
        """
        """
        - SET `all_suits` with returning list from `get_suits`
        - return result of `check_suit(all_suits)`
        """
        all_suits = self.get_suits()
        return self.check_suit(all_suits)

    def _is_straight(self):
        """
        # 6
        5 consecutive cards but with different suits
        Highest: A K Q J 10
        Lowest: 5 4 3 2 A ("wheel")
        """
        """
        VIS:
        So we want these combos:
        2 3 4 5 6
        3 4 5 6 7
        4 5 6 7 8
        5 6 7 8 9
        6 7 8 9 10
        7 8 9 10 11
        8 9 10 11 12
        9 10 11 12 13
        10 11 12 13 14

        RULES:
        - all 5 values (ranks) have to be distinct
        - the ranks have to be consecutive (difference of 1)

        BRAINSTORM:
        - check for duplicates
            - if there are duplicates, then return False
        - sort it by ascending order
            - check if adding 1 to each number produces the same number as the
              card after it
        
        ALGO:
        - SET `all_ranks` with returning list from `get_ranks()`
        - SET `numeric_ranks` with returning list from 
              `convert_to_numeric(all_ranks)`
        - sort values in ascending order
        - if `check_duplicates(numeric_ranks)` returns True (yes, duplicates):
            - return False
        - return boolean from `check_consecutive(numeric_ranks)`
        """
        # TODO: Extract me from here
        all_ranks = self.get_ranks()
        numeric_ranks = self.convert_to_numeric(all_ranks)
        numeric_ranks.sort()
        # TODO: to here (maybe)

        if self.check_duplicates(numeric_ranks):
            return False

        return self.check_consecutive(numeric_ranks)

    def check_duplicates(self, numeric_ranks):
        """
        Returns True if there are duplicates, False otherwise.
        I: a list, of ranks as integers
        O: boolean
        
        - SET `seen` with an empty set
        - for `rank` in `numeric_ranks`:
            - if `rank` is already in `seen`:
                return True
            - add `rank` to `seen`
        - return False
        """
        seen = set()
        for rank in numeric_ranks:
            if rank in seen:
                return True
            seen.add(rank)

        return False

    def _is_three_of_a_kind(self):
        """
        # 7
        3 cards of the same rank & 2 unrelated cards
        7S 7D 7C KC 3D 
        """
        """
        RULES:
        - 3 of one rank
        - remaining 2 cards must be:
            - different ranks from each other
            - different rank from the triple
        [NOTE: Be careful not to return True for a full house]
        
        ALGO:
        - SET `all_ranks` with ranks of all cards as a list
        - SET `rank_counts` with a frequency count of all the ranks
        - turn the collection of counts in `rank_counts` into a list
        - sort this list in ascending order
        - if it matches `[1, 1, 3]`:
                - return True
        - return False
        """
        all_ranks = self.get_ranks()
        rank_counts = list(self.count_ranks(all_ranks).values())
        rank_counts.sort()

        return rank_counts == [1, 1, 3]

    def _is_two_pair(self):
        """
        # 8
        2 cards with same rank in pairs & a different kind ("kicker")
        4S 4C 3S 3D QS
        """
        """
        RULES:
        - 2 cards share the same rank
        - another pair of 2 cards share the same rank (disctinct from previous 
          pair)
        
        ALGO:
        - SET `all_ranks` with ranks of all cards as a list
        - SET `rank_counts` with a frequency count of all the ranks
        - turn the collection of counts in `rank_counts` into a list
        - sort it in ascending order
        - if it matches `[1, 2, 2]`:
            - return true
        - return false
        """
        all_ranks = self.get_ranks()
        rank_counts = list(self.count_ranks(all_ranks).values())
        rank_counts.sort()

        return rank_counts == [1, 2, 2]

    def _is_pair(self):
        """
        # 9
        2 cards of same rank & 3 independent cards
        AH AD 8S 4C 7H
        """
        """
        RULES:
        - 2 cards share the same rank
        - 3 cards have distinct ranks from each other & above pair

        ALGO:
        - SET `all_ranks` with ranks of all cards as a list
        - SET `rank_counts` with a frequency count of all the ranks
        - turn the collection of counts in `rank_counts` into a list
        - sort it in ascending order
        - if it matches `[1, 1, 1, 2]`:
            - return true
        - return false
        """
        all_ranks = self.get_ranks()
        rank_counts = list(self.count_ranks(all_ranks).values())
        rank_counts.sort()

        return rank_counts == [1, 1, 1, 2]

# Test code
hand = PokerHand(Deck())  # from "real" shuffled deck
hand.print()
# print(hand.evaluate()) TODO: UNCOMMENT ME
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
