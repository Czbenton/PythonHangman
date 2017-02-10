import GameLogic
import Graphics

print(Graphics.board1, sep="\n")

print(GameLogic.gameWord) #todo cheat mode

GameLogic.createGameBoard()
print(GameLogic.rightGuesses)
while "_" in GameLogic.rightGuesses:
    GameLogic.makeAGuess()
