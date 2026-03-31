class Game:
    count = 0

    def __init__(self, game_type):
        self.game_type = game_type
        Game.count += 1

    def play(self):
        return f'Start the {self.game_type} game!'

    @classmethod
    def return_count(cls):
        return cls.count

class Bingo(Game):
    def __init__(self, game_type, player_name):
        super().__init__(game_type)
        self.player_name = player_name

class Scrabble(Game):
    def __init__(self, game_type, player_name1, player_name2):
        super().__init__(game_type)
        self.player_name1 = player_name1
        self.player_name2 = player_name2

bingo = Bingo('Bingo', 'Bill')
print(Game.count)                       # 1
print(bingo.play())                     # Start the Bingo game!
print(bingo.player_name)                # Bill

scrabble = Scrabble('Scrabble', 'Jill', 'Sill')
print(Game.count)                       # 2
print(scrabble.play())                  # Start the Scrabble game!
print(scrabble.player_name1)            # Jill
print(scrabble.player_name2)            # Sill
print(scrabble.player_name)
# AttributeError: 'Scrabble' object has no attribute 'player_name'
