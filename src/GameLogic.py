import random

rightGuesses = []
wrongGuesses = []


def selectRandomWord():
    array = []
    with open("words.txt", "r") as f:
        for line in f:
            array.append(line.strip())

    x = random.randrange(1, 354939)
    randomWord = array[x]
    return randomWord


gameWord = list(selectRandomWord())


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


