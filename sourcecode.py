from turtle import speed, pu, pd, goto, setheading, fd, lt, rt, circle, done
from math import sqrt
from random import choice

# I imported functions from the turtle, math, and random modules

def displayBoard(x):
    speed('fastest')
    pu()
    goto(600/x-300, -300)
    i = 1
    while i < x:
        setheading(90)
        pd()
        fd(600)
        pu()
        lt(135)
        fd(i*600/x*sqrt(2))
        lt(135)
        pd()
        fd(600)
        pu()
        rt(90)
        fd(600/x)
        rt(45)
        fd((600-600/x*(i+1))*sqrt(2))
        i += 1
    return

# I defined a function that, when called, draws an empty Tic-Tac-Toe board with the dimensions that the player specified

def displayBoardMove(board, x):
    goto(boardDict[board[-2]])
    setheading(90)
    fd(200/x)
    rt(90)
    fd(200/x)
    rt(135)
    pd()
    fd(400/x*sqrt(2))
    pu()
    rt(135)
    fd(400/x)
    rt(135)
    pd()
    fd(400/x*sqrt(2))
    pu()
    goto(boardDict[board[-1]])
    setheading(0)
    fd(200/x)
    lt(90)
    pd()
    circle(200/x)
    pu()
    return

# I defined a function that, when called, marks the latest move that the player and computer made

def displayFinishingBoardMove(board, x):
    goto(boardDict[board[-1]])
    setheading(90)
    fd(200/x)
    rt(90)
    fd(200/x)
    rt(135)
    pd()
    fd(400/x*sqrt(2))
    pu()
    rt(135)
    fd(400/x)
    rt(135)
    pd()
    fd(400/x*sqrt(2))
    pu()

# I defined a function that, when called, displays the lastest move that the player made if that move won them the game. Therefore, it doesn't include a move made by the computer.

def checkIfLegal(number, board, x):
    if int(number) < 1 or int(number) > x**2 or int(number) in board:
        return False

# I defined a function that, when called, checks if the cell that the player just inputted is part of the Tic-Tac-Toe board and hasn't been played yet

def checkWinner(board, x):
    for i in range(x):
        if all(item in board for item in boardMatrix[i]):
            return True
        column = []
        for row in boardMatrix:
            column.append(row[i])            
        if all(item in board for item in column):
            return True
        diagonal1 = []
        for i in range(x):
            diagonal1.append(boardMatrix[i][i])
        if all(item in board for item in diagonal1):
            return True
        diagonal2 = []
        for i in range(x):
            diagonal2.append(boardMatrix[i][-i-1])
        if all(item in board for item in diagonal2):
            return True
        if x % 2 != 0:
            if len(board) == (x**2)//2+1:
                return False
        if x % 2 == 0:
            if len(board) == x**2/2:
                return False

# I defined a function that, when called, checks whether the latest move that the player made resulted in a filled row, column, or diagonal. If none of these are true and the user has picked the last available cell on the board, the game ends in a tie.

def computerMove(board):
    return choice([i for i in range(1,26) if i not in board])

# I defined a function that, when called, causes the computer to pick a random cell on the board that hasn't been played yet

def smartComputerMove(board, x):
    if len(board) == 1:
        if x % 2 != 0:
            if board[-1] == (x**2)//2+1:
                return choice([1, x, x**2+1-x, x**2])
            else:
                return (x**2)//2+1
        else:
            return choice([i for i in range(1,1+x**2) if i not in board])

# If the first play cell that the user picks is in the centre of the board, then the computer randomly picks a corner cell. If the first play is anywhere else, the computer picks the centre cell. If the dimensions of the board are even, then the computer randomly picks a cell that hasn't been played yet.

    else:
        for i in range(x):
            if len(set(board[0::2]).intersection(set(boardMatrix[i]))) == x-1:
                if len(set(boardMatrix[i]).difference(set(board))) != 0:
                    return list(set(boardMatrix[i]).difference(set(board[0::2])))[0]
            column = []
            for row in boardMatrix:
                column.append(row[i])
            if len(set(board[0::2]).intersection(set(column))) == x-1:
                if len(set(column).difference(set(board))) != 0:
                    return list(set(column).difference(set(board[0::2])))[0]
            diagonal1 = []
            for i in range(x):
                diagonal1.append(boardMatrix[i][i])
            if len(set(board[0::2]).intersection(set(diagonal1))) == x-1:
                if len(set(diagonal1).difference(set(board))) != 0:
                    return list(set(diagonal1).difference(set(board[0::2])))[0]
            diagonal2 = []
            for i in range(x):
                diagonal2.append(boardMatrix[i][-i-1])
            if len(set(board[0::2]).intersection(set(diagonal2))) == x-1:
                if len(set(diagonal2).difference(set(board))) != 0:
                    return list(set(diagonal2).difference(set(board[0::2])))[0]

# If there is any row, column, or diagonal where there is a move that would make the player a winner, the computer will block the last cell to block the player from winning

            if len(set(board[1::2]).intersection(set(boardMatrix[i]))) == x-1:
                if len(set(boardMatrix[i]).difference(set(board))) != 0:
                    return list(set(boardMatrix[i]).difference(set(board[1::2])))[0]
            if len(set(board[1::2]).intersection(set(column))) == x-1:
                if len(set(column).difference(set(board))) != 0:
                    return list(set(column).difference(set(board[1::2])))[0]
            if len(set(board[1::2]).intersection(set(diagonal1))) == x-1:
                if len(set(diagonal1).difference(set(board))) != 0:
                    return list(set(diagonal1).difference(set(board[1::2])))[0]
            if len(set(board[1::2]).intersection(set(diagonal2))) == x-1:
                if len(set(diagonal2).difference(set(board))) != 0:
                    return list(set(diagonal2).difference(set(board[1::2])))[0]

# If there isn't a move that would make the player a winner, then if there is any row, column, or diagonal where there is a move that would make the computer a winner, the computer will pick the 5th cell

        else:
            return choice([i for i in range(1,1+x**2) if i not in board])

# If neither options are available, then the computer randomly picks a cell that hasn't been played yet

def main(x):
    print("\nHello and welcome to the Tic-Tac-Toe Comp 208 challenge: Player against Computer.\n\nThe board is numbered from 1 to " + str(x**2) + ".\n")
    print("Player starts first. Simply input the number of the cell you want to occupy. Player's move is marked with X. Computer's move is marked with O.\n")
    print("Start? (y/n):")
    response = input()

# When the program starts, an introductory message appears and asks the player if they want to continue or not. If they enter 'n', the program ends. If they enter 'y', the program continues, and the game starts.

    if response == "n":
        exit()
    if response == "y":
        displayBoard(x)
        res = []
        while 1 == 1:

# Until the player or computer wins or the game ends in a tie, the program loops, asking the player to pick a cell, checking if the play is legal, checking if the player or computer won or the game ended in a tie, and displaying the plays

            number = int(input("\nWhich cell would you like to occupy: "))
            if checkIfLegal(number, res, x) == False:
                print("\nYou entered an illegal move. Please enter a different cell number.")

# This calls the checkIfLegal function

            else:
                res.append(number)

# The latest move that the player made is added to the list of moves made

                resPlayer = res[0::2]
                if checkWinner(resPlayer, x) == False:
                    print("\nIt's a tie. Better luck next time.")
                    displayFinishingBoardMove(res, x)
                    done()
                    exit()

# This calls the checkWinner function to check if the player made the last move on the board without winning. If they did, the finishing move is displayed.

                if checkWinner(resPlayer, x) == True:
                    print("\nCongratulations. Player wins.")
                    displayFinishingBoardMove(res, x)
                    done()
                    exit()

# This calls the checkWinner function to check if the player made the last move on the board. If they did, the finishing move is displayed.

                '''
                res.append(computerMove(res))
                '''
                res.append(smartComputerMove(res, x))
                resComputer = res[1::2]

# The latest move that the computer made is added to the list of moves made

                if checkWinner(resComputer, x) == True:
                    print("\nComputer wins. Better luck next time.")
                    displayBoardMove(res, x)
                    done()
                    exit()

# This calls the checkWinner function to check if the computer won after its move. If it did, the player's and computer's final move is displayed.

                displayBoardMove(res, x)

# If none of the other conditions are satisfied, Turtle module displays the latest moves from the player and computer, and the loop starts again.

dimension = int(input("Please enter the dimension of the Tic-Tac-Toe board: "))

# When it starts, the program asks the player what they want the dimensions of their board to be. The resulting input is used as a variable in all my defined functions.

boardDict = dict()
for i in range(dimension):
    for j in range(dimension):
        boardDict[dimension*i+j+1] = (300/dimension+600/dimension*j+-300, 300-300/dimension-600/dimension*i)
    
# I created a dictionary whose values are coordinates on the Turtle module, each with a index (1 to the specified dimension squared) identifying which number on the board it corresponds to
    
boardMatrix = [[dimension*i+j+1 for j in range(dimension)] for i in range(dimension)]
    
# I also created a matrix to help identify which column and row each number on the board belongs to. This is useful for defining my displayBoardMove, displayFinishingBoardMove, checkWinner, and smartComputerMove definition.
    
main(dimension)
    
# This starts the game
