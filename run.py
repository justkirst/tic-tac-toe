import random

# Setup

yes_no = ["yes", "no"]
response = ""

# Start of the game and instructions

name = ""
while name == "" :
    name = input("What is your name?\n")
    if not name.isalpha():
        print ("Please enter a valid name")
print("Hi " + name + "!")

while response not in yes_no:
    response = input("Would you like to start a new game?\n Yes or No?\n")
    if response == "yes":
        print("Great! Let's get started!")
    elif response == "no":
        print("Not to worry. You can come back at a later date to play!")
        quit()
    else:
        print("I didn't understand that.\n")

# Functions to build the board and let the player choose their playing piece

def players_board(board):
    """
    This function builds the Tic Tac Toe board.
    """
    blank_board="""
___________________
|     |     |     |
| 1 |   2 |   3  |
|     |     |     |
|-----------------|
|     |     |     |
|  4  |  5  |  6  |
|     |     |     |
|-----------------|
|     |     |     |
|  7  |  8  |  9  |
|     |     |     |
|-----------------|
"""

    for i in range(1,10):
        if (board[i] == "O" or board[i] == "X"):
            blank_board = blank_board.replace(str(i), board[i])
        else:
            blank_board = blank_board.replace(str(i), "")
    print(blank_board)

def players_letter():
    """
    Let's the player choose which letter to play with. 
    Program will then return the players letter first and the computer's letter second.
    """
    letter = ""
    while not (letter == 'X' or letter == 'O'):
        print("Do you want to play as X or O?\n")
        letter = input().upper()
    
    if letter == "X":
        return ["X", "O"]
    else:
        return ["O", "X"]

def first_player():
    """
    Random function to randomly choose the player who goes first.
    """
    if random.randint(0, 1) == 0:
        return "Computer goes first"
    else:
        return "Player goes first"    