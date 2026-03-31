class Game:
    count = 0

    def __init__(self, game_type, player_name):
        self.game_type = game_type
        self.player_name = player_name
        self.__class__.count += 1

    def play(self):
        return 'Start the game!'

class Bingo(Game):
    pass

bingo = Bingo('Bingo', 'Bill')
print(Game.count)                       # 1
print(bingo.play())                     # Start the Bingo game!
print(bingo.player_name)                # Bill

# scrabble = Scrabble('Scrabble', 'Jill', 'Sill')
# print(Game.count)                       # 2
# print(scrabble.play())                  # Start the Scrabble game!
# print(scrabble.player_name1)            # Jill
# print(scrabble.player_name2)            # Sill
# print(scrabble.player_name)
# # AttributeError: 'Scrabble' object has no attribute 'player_name'
