# board1 = (
#     "-----------\n",
#     " |        |\n",
#     "          |\n",
#     "          |\n",
#     "          |\n",
#     "          |\n",
#     "          |\n",
#     "------------------------\n")
#
# board2 = (
#     "-----------\n",
#     " |        |\n",
#     " ()       |\n",
#     "          |\n",
#     "          |\n",
#     "          |\n",
#     "          |\n",
#     "------------------------\n")
#
# board3 = (
#     "-----------\n",
#     " |        |\n",
#     " ()       |\n",
#     "\\         |\n",
#     "          |\n",
#     "          |\n",
#     "          |\n",
#     "------------------------\n")
#
# board4 = (
#     "-----------\n",
#     " |        |\n",
#     " ()       |\n",
#     "\\|        |\n",
#     "          |\n",
#     "          |\n",
#     "          |\n",
#     "------------------------\n")
#
# board5 = (
#     "-----------\n",
#     " |        |\n",
#     " ()       |\n",
#     "\\||       |\n",
#     "          |\n",
#     "          |\n",
#     "          |\n",
#     "------------------------\n")
#
# board6 = (
#     "-----------\n",
#     " |        |\n",
#     " ()       |\n",
#     "\\||/      |\n",
#     "          |\n",
#     "          |\n",
#     "          |\n",
#     "------------------------\n")
#
# board7 = (
#     "-----------\n",
#     " |        |\n",
#     " ()       |\n",
#     "\\||/      |\n",
#     " |        |\n",
#     "          |\n",
#     "          |\n",
#     "------------------------\n")
#
# board8 = (
#     "-----------\n",
#     " |        |\n",
#     " ()       |\n",
#     "\\||/      |\n",
#     " ||       |\n",
#     "          |\n",
#     "          |\n",
#     "------------------------\n")
#
# baord9 = (
#     "-----------\n",
#     " |        |\n",
#     " ()       |\n",
#     "\\||/      |\n",
#     " ||       |\n",
#     "/         |\n",
#     "          |\n",
#     "------------------------\n")
# board10 = (
#     "-----------\n",
#     " |        |\n",
#     " ()       |\n",
#     "\\||/      |\n",
#     " ||       |\n",
#     "/  \\      |\n",
#     "          |\n",
#     "------------------------\n")


def printGameBoard(counter):
    if counter == 10:
        gameboard = "---------\n      |\n      |\n      |\n      |\n      |\n_________"
    elif counter == 9:
        gameboard = "---------\n    | |\n      |\n      |\n      |\n      |\n_________"
    elif counter == 8:
        gameboard = "---------\n    | |\n   () |\n      |\n      |\n      |\n_________"
    elif counter == 7:
        gameboard = "---------\n    | |\n   () |\n  \   |\n      |\n      |\n_________"
    elif counter == 6:
        gameboard = "---------\n    | |\n   () |\n  \|  |\n      |\n      |\n_________"
    elif counter == 5:
        gameboard = "---------\n    | |\n   () |\n  \|| |\n      |\n      |\n_________"
    elif counter == 4:
        gameboard = "---------\n    | |\n   () |\n  \||/|\n      |\n      |\n_________"
    elif counter == 3:
        gameboard = "---------\n    | |\n   () |\n  \||/|\n   /  |\n      |\n_________"
    elif counter == 2:
        gameboard = "---------\n    | |\n   () |\n  \||/|\n   /\ |\n      |\n_________"
    elif counter == 1:
        gameboard = "---------\n    | |\n   () |\n  \||/|\n   /\ |\n  /   |\n_________"
    else:
        gameboard = "---------\n    | |\n   () |\n  \||/|\n   /\ |\n  /  \|\n_________"

    print(gameboard)