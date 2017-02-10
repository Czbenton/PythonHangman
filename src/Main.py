import AvailableWords

rightGuesses = []
wrongGuesses = []

AvailableWords.populateAvailableWords()
gameWord = list(AvailableWords.selectRandomWord())

for x in range(len(gameWord)):
    rightGuesses.append("_")

print(gameWord)
print(rightGuesses)

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

while "_" in rightGuesses:
    makeAGuess()
