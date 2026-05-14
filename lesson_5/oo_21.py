import random
DASHES = '-' * 60

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
        self.hand = []

    def add_card(self, card):
        self.hand.append(card)

    def display_hand(self):
        num_of_cards = len(self.hand)

        match num_of_cards:
            case 0:
                return 'No cards in hand'
            case 1:
                return str(self.hand[0])
            case 2:
                return f'{self.hand[0]} and {self.hand[1]}'
            case _:
                last = str(self.hand[-1])
                first = self.hand[:-1]
                card_list = [str(card) for card in first]
                first = ', '.join(card_list)
                return f'{first}, and {last}'

    def hit(self, deck):
        print(f'{self} chose hit.')
        new_card = deck.draw()
        print(f'{self} drew: {new_card}')
        self.hand.append(new_card)

    def is_busted(self):
        return self.total_points() > 21

    def total_points(self):
        card_ranks = [card.rank for card in self.hand]

        score = 0
        for rank in card_ranks:
            if rank == 'Ace':
                score += 1
            elif rank in ['Jack', 'Queen', 'King']:
                score += 10
            else:
                score += rank

        number_of_aces = card_ranks.count('Ace')
        for _ in range(number_of_aces):
            if score + 10 <= 21: # Update ace to 11 if it won't cause a bust.
                score += 10

        return score

class Player(Participant):
    # TODO: FINISH ME!!
    def __init__(self):
        # STUB
        # A player needs, in addition to the ones in Participant:
        # betting money (starts at $5)
        super().__init__()

    def __str__(self):
        return 'You'

class Dealer(Participant):

    def display_hand(self, hide_one=False):
        if hide_one:
            return f'{self.hand[0]} and [Hidden Card]'
        return super().display_hand()

    def __str__(self):
        return 'Dealer'

class TwentyOneGame:

    def __init__(self):
        self.deck = Deck()
        self.player = Player()
        self.dealer = Dealer()

    def start(self):
        # SPIKE
        self.display_welcome_message()
        self.deal_cards()
        self.show_cards()
        self.player_turn()

        if not self.player.is_busted():
            self.dealer_turn()

        self.display_result()
        self.display_goodbye_message()

    def deal_cards(self):
        for _ in range(2):
            self.player.add_card(self.deck.draw())
            self.dealer.add_card(self.deck.draw())

    def show_cards(self):
        print(DASHES)
        print(f"Dealer's Hand: {self.dealer.display_hand(True)}")
        print(f"Your Hand: {self.player.display_hand()}")
        print(f"Your Point Total: {self.player.total_points()}")
        print(DASHES)

    def player_turn(self):
        print("| PLAYER TURN |")

        while True:
            prompt = "==> Hit or Stay? Enter 'h' for Hit & 's' for Stay: "
            player_choice = input(prompt).strip().lower()

            if player_choice not in ['h', 's']:
                print('Invalid input. Please try again.')
                continue

            if player_choice == 'h':
                self.player.hit(self.deck)
                self.show_cards()

            if self.player.is_busted():
                return

            if player_choice == 's':
                print('You chose to stay.')
                print(DASHES)
                return

    def dealer_turn(self):
        # STUB
        print("| DEALER TURN |")

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
# deck = Deck()
# print(deck.cards)
# print(len(deck.cards))
