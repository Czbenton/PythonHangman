import GameLogic
import Graphics

print(GameLogic.gameWord)  # todo cheat mode

GameLogic.createGameBoard()
print(GameLogic.rightGuesses)
counter = 0
while "_" in GameLogic.rightGuesses:
    counter = GameLogic.makeAGuess(counter)
    print(counter)
    Graphics.printGallows(counter)
    if counter == 10:
        break

print("Game over!!")
