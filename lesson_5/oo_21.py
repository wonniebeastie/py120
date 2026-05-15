import random
import os
DASHES = '-' * 60

def clear_screen():
    os.system('clear')

class Card:
    SUITS = ('Hearts', 'Diamonds', 'Clubs', 'Spades')
    RANKS = ('Ace', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'Jack', 'Queen', 'King')

    def __init__(self, suit, rank):
        self._suit = suit
        self._rank = rank

    @property
    def suit(self):
        return self._suit

    @property
    def rank(self):
        return self._rank

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
        print(f'{self} chose to hit.')
        new_card = deck.draw()
        print(f'{self} drew: {new_card}')
        self.hand.append(new_card)

    def is_busted(self):
        return self.total_points > 21

    @property
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
    def __init__(self):
        super().__init__()
        self.money = 5

    def __str__(self):
        return 'You'

class Dealer(Participant):

    def display_hand(self, hide_one=False):
        if hide_one:
            return f'{self.hand[0]} and [Hidden Card]'
        return super().display_hand()

    def show_dealer_info(self):
        print(
            f"Dealer's Hand: {self.display_hand()} | "
            f"Dealer's Point Total: {self.total_points}"
        )

    def __str__(self):
        return 'Dealer'

class TwentyOneGame:

    def __init__(self):
        self.deck = Deck()
        self.player = Player()
        self.dealer = Dealer()

    def start(self):
        self.display_welcome_message()

        while True:
            self.play_round()

            financial_status = self.broke_or_rich()

            if financial_status == 'broke':
                print(f"You're now too {financial_status} to play.")
                break

            if financial_status == 'rich':
                print(f"You can now go home {financial_status}!")
                break

            if not self.play_again():
                break

            print("Let's go again!")
            clear_screen()
            self.reset_round()

        self.display_goodbye_message()

    def play_round(self):
        self.deal_cards()
        self.show_cards()
        self.player_turn()

        if not self.player.is_busted():
            self.dealer_turn()

        self.display_result()

    def deal_cards(self):
        for _ in range(2):
            self.player.add_card(self.deck.draw())
            self.dealer.add_card(self.deck.draw())

    def show_cards(self):
        print(DASHES)
        print(f"Dealer's Hand: {self.dealer.display_hand(True)}")
        print(f"Your Hand: {self.player.display_hand()} | "
              f"Your Point Total: {self.player.total_points}")
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
                print('You busted!')
                return

            if player_choice == 's':
                print('You chose to stay.')
                print(DASHES)
                return

    def dealer_turn(self):
        print('| DEALER TURN |')
        self.dealer.show_dealer_info()

        while self.dealer.total_points < 17:
            self.dealer.hit(self.deck)
            print(DASHES)
            self.dealer.show_dealer_info()

        if self.dealer.is_busted():
            print('Dealer busted!')
            print(DASHES)
            return

        print('Dealer stays.')
        print(DASHES)
        return

    def determine_winner(self, player_points, dealer_points):
        if player_points > dealer_points:
            return 'player'

        if player_points < dealer_points:
            return 'dealer'

        return 'tie'

    def display_welcome_message(self):
        print("Welcome to a game of Twenty-One. Let's play!")
        print()
        print(f"You have ${self.player.money} to start. \n"
              f"If you reach $0, you will be kicked out of the game. \n"
              f"However, if you reach $10, you get to go home rich.")

    def display_goodbye_message(self):
        print()
        print('Thanks for playing Twenty-One. Goodbye.')

    def display_result(self):
        player_points = self.player.total_points
        dealer_points = self.dealer.total_points
        winner = None

        print(f"Your Points: {player_points} | "
              f"Dealer's Points: {dealer_points}")

        if self.player.is_busted():
            winner = 'dealer'
        elif self.dealer.is_busted():
            winner = 'player'
        else:
            # If both stayed
            winner = self.determine_winner(player_points, dealer_points)

        if winner == 'player':
            self.player.money += 1
            print(f'You now have ${self.player.money}.')
            print('Congratulations, you won the round!')
        elif winner == 'dealer':
            self.player.money -= 1
            print(f'You now have ${self.player.money}.')
            print('Dealer wins this round, better luck next time.')
        else:
            print("It's a tie!")

    def play_again(self):
        while True:
            answer = input("==> Play again? Enter 'y' or 'n': ").strip().lower()

            if answer in ['y', 'n']:
                break

            print("Please enter a valid choice.")

        return answer == 'y'

    def reset_round(self):
        self.deck = Deck()
        self.player.hand = []
        self.dealer.hand = []

    def broke_or_rich(self):
        if self.player.money == 0:
            return 'broke'

        if self.player.money == 10:
            return 'rich'

        return None

game = TwentyOneGame()
game.start()
