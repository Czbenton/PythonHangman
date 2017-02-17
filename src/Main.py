import GameLogic
import Graphics

print(GameLogic.gameWord, "cheat mode on")  # todo cheat mode

GameLogic.createGameBoard()
print(GameLogic.rightGuesses)
counter = 0
while True:
    counter = GameLogic.makeAGuess(counter)
    Graphics.printGallows(counter)
    if counter == 10:
        break

print("Game over!!")
