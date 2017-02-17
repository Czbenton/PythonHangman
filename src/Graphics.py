def printGallows(counter):
    if counter == 1:
        gallows = "---------\n      |\n      |\n      |\n      |\n      |\n_________"
    elif counter == 2:
        gallows = "---------\n    | |\n      |\n      |\n      |\n      |\n_________"
    elif counter == 3:
        gallows = "---------\n    | |\n   () |\n      |\n      |\n      |\n_________"
    elif counter == 4:
        gallows = "---------\n    | |\n   () |\n  \   |\n      |\n      |\n_________"
    elif counter == 5:
        gallows = "---------\n    | |\n   () |\n  \|  |\n      |\n      |\n_________"
    elif counter == 6:
        gallows = "---------\n    | |\n   () |\n  \|| |\n      |\n      |\n_________"
    elif counter == 7:
        gallows = "---------\n    | |\n   () |\n  \||/|\n      |\n      |\n_________"
    elif counter == 8:
        gallows = "---------\n    | |\n   () |\n  \||/|\n   /  |\n      |\n_________"
    elif counter == 9:
        gallows = "---------\n    | |\n   () |\n  \||/|\n   /\ |\n      |\n_________"
    elif counter == 10:
        gallows = "---------\n    | |\n   () |\n  \||/|\n   /\ |\n  /   |\n_________"
    else:
        gallows = "---------\n    | |\n   () |\n  \||/|\n   /\ |\n  /  \|\n_________"

    print(gallows)
