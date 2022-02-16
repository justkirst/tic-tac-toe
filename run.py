import random

# Setup

yes_no = ["y", "n"]

# Start of the game and instructions

def game_setup():
    name = ""
    while name == "" :
        name = input("What is your name?\n")
        if not name.isalpha():
            print ("Please enter a valid name without any special characters.")
    print("Hi " + name + "!")

    response = ""
    while response not in yes_no:
        response = input("Would you like to start a new game?\n (Y)es or (N)o?\n")
        if response == "yes":
            print("Great! Let's get started!")
            game_intro()
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
    while not (letter == "X" or letter == "O"):
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
        return "computer"
    else:
        return "player"  

def new_game():
    """
    This function will create a new game if value returns true
    """  
    response = ""
    while response not in yes_no:
        response = input("Do you want to play again?\n Yes or No\n")
    if response == "y":
        print("Great! Let's play again")
        game_intro()
    elif response == "n":
        print("Not to worry. You can come back at a later date to play!")
        quit()
    else:
        print("I didn't understand that.\n")


def make_move(board, letter, move):
    board[move] = letter

def winner(bo, le):
    """
    Depending on the board and the player's letter, this function will return True if that player has won.
    """
    return ((bo[1] == le and bo[2] == le and bo[3] == le) or # across the top
    (bo[4] == le and bo[5] == le and bo[6] == le) or # across the middle
    (bo[7] == le and bo[8] == le and bo[9] == le) or # across the bottom
    (bo[1] == le and bo[4] == le and bo[7] == le) or # down the left side
    (bo[2] == le and bo[5] == le and bo[8] == le) or # down the middle
    (bo[3] == le and bo[6] == le and bo[9] == le) or # down the right side
    (bo[3] == le and bo[5] == le and bo[7] == le) or # diagonal
    (bo[1] == le and bo[5] == le and bo[9] == le)) # diagonal

def copy_board(board):
    """
    Duplicate the board and return it as the duplicate.
    """
    dupe_board = []

    for i in board:
        dupe_board.append(i)

    return dupe_board

def free_space(board, move):
    """
    Function to return true if the requested next move is free on the current board.
    """
    return board[move] == ""

def player_move(board):
    """
    This function allows the playter to choose their next move.
    """
    move = ""
    while move not in "1 2 3 4 5 6 7 8 9".split() or not free_space(board, int(move)):
        print("What is your next move? (1-9)")
        move = input()
    return int(move)

def random_move(board, moves_list):
    """
    Function will return a valid move from the current board.
    """
    possible_moves = []
    for i in moves_list:
        if free_space(board, i):
            possible_moves.append(i)

    if len(possible_moves) != 0:
        return random.choice(possible_moves)
    else:
        return None

def computer_move(board, computer_letter):
  
    if computer_letter == "X":
        player_letter = "O"
    else:
        player_letter = "X"

    for i in range(1, 10):
        copy = copy_board(board)
        if free_space(copy, i):
            make_move(copy, computer_letter, i)
            if winner(copy, computer_letter):
                return i

    for i in range(1, 10):
        copy = copy_board(board)
        if free_space(copy, i):
            make_move(copy, player_letter, i)
            if winner(copy, player_letter):
                return i

    move = random_move(board, [1, 3, 7, 9])
    if move is not None:
        return move

    if free_space(board, 5):
        return 5

    return random_move(board, [2, 4, 6, 8])

def full_board(board):
    # Return True if every space on the board has been taken. Otherwise return False.
    for i in range(1, 10):
        if free_space(board, i):
            return False
    return True

def game_intro():
    print("  _                  _                                            ")
print(" (_|   |   |_/      | |                                           ")
print("   |   |   |    _   | |   __    __    _  _  _     _     _|_   __  ")
print("   |   |   |   |/   |/   /     /  \_ / |/ |/ |   |/      |   /  \_")
print("    \_/ \_/    |__/ |__/ \___/ \__/    |  |  |_/ |__/    |_/ \__/ ")


print("______              ______                 ______           ")
print(" (_) |   o           (_) |                  (_) |             ")
print("     |        __         |    __,    __         |    __    _  ")
print("   _ |   |   /         _ |   /  |   /         _ |   /  \_ |/  ")
print("   (_/    |_/ \___/    (_/    \_/|_/ \___/    (_/    \__/  |__/")

while True:
    """
    Function for reseting the board
    """
    the_board = [""] * 10
    player_letter, computer_letter = players_letter()
    turn = first_player()
    print("The " + turn + " will go first.")
    game_play = True

    while game_play:
        if turn == "player":
            players_board(the_board)
            move = player_move(the_board)
            make_move(the_board, player_letter, move)

            if winner(the_board, player_letter):
                players_board(the_board)
                print("Woohoo! You have won the game!")
                game_play = False
            else:
                if full_board(the_board):
                    players_board(the_board)
                    print("This game was a tie. Better luck next time!")
                    break
                else:
                    turn = "computer"

        else:
            move = computer_move(the_board, computer_letter)
            make_move(the_board, computer_letter, move)

            if winner(the_board, computer_letter):
                players_board(the_board)
                print("The computer beat you! You lose. Better luck next time!")
                game_play = False
            else:
                if full_board(the_board):
                    players_board(the_board)
                    print("This game was a tie. Better luck next time!")
                    break
                else:
                    turn = "player"

    if not new_game():
        break
game_intro()