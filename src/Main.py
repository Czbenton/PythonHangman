import GameLogic

rightGuesses = []
wrongGuesses = []
gameWord = list(GameLogic.selectRandomWord())


def createGameBoard():
    for x in range(len(gameWord)):
        rightGuesses.append("_")


def makeAGuess():
    userGuess = input("Please enter a guess!\n")
    if userGuess in gameWord:
        for x in range(len(gameWord)):
            if userGuess == gameWord[x]:
                rightGuesses[x] = userGuess
    else:
        wrongGuesses.append(userGuess)
        print("Wrong. Try again.", wrongGuesses)

    print(rightGuesses)


print(gameWord) #todo cheat mode

createGameBoard()
print(rightGuesses)
while "_" in rightGuesses:
    makeAGuess()
