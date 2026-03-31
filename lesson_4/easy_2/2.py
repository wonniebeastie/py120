class Game:
    def play(self):
        return 'Start the game!'

class Bingo(Game):
    pass

game1 = Bingo()
print(game1.play()) # Start the game!
