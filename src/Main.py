import GameLogic
import Graphics

print(GameLogic.gameWord)  # todo cheat mode

GameLogic.createGameBoard()
print(GameLogic.rightGuesses)
counter = 0
while "_" in GameLogic.rightGuesses:
    GameLogic.makeAGuess(counter)
    counter = GameLogic.inc(counter)

print("Game over!")
