import random

array = []


def populateAvailableWords():
    with open("words.txt", "r") as f:
        for line in f:
            array.append(line.strip())


def selectRandomWord():
    x = random.randrange(1, 354939)
    randomWord = array[x]
    return randomWord
