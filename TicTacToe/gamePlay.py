import random

board = []

row = 0
column = 0
seed = 'X'

def initBoard():
    num = 9
    for i in range(3):
        board.append([])
        for j in range(3):
            board[i].append(' ')
            num -= 1

def showTheBoard():
    print "The Board:"
    print "--------------"
    for i in range(3):
        print "|",
        for j in range(3):
            print board[i][j], "|",
        print
        print "|   |   |   |"
        print "--------------"

def drawSeed(row, column, seed):
    board[row][column] = seed

def playerMove(seed):
    pMove = int(raw_input("Enter your move(1 to 9): "))
    pMove -= 1
    row = pMove/3; column = pMove%3
    if not isValid(row, column):
        print "Invalid Move"
        return
    board[pMove/3][pMove%3] = seed

def play():
    pos = 0
    while not boardIsFilled() and not result():
        print "Player ",(pos%2+1), " move: "
        playerMove(player[pos%2])
        showTheBoard()
        pos += 1
        print "Player ", ((pos-1) % 2 + 1), " wins"

def isValid(row, column):
    return board[row][column] == ' '

def boardIsFilled():
    return not(' ' in board[0] or ' ' in board[1] or ' ' in board[2])

def result():
    if board[0][0] == board[0][1] == board[0][2] != ' ':
        return True
    elif board[1][0] == board[1][1] == board[1][2] != ' ':
        return True
    elif board[2][0] == board[2][1] == board[2][2] != ' ':
        return True
    elif board[0][0] == board[1][0] == board[2][0] != ' ':
        return True
    elif board[0][1] == board[1][1] == board[2][1] != ' ':
        return True
    elif board[0][2] == board[1][2] == board[2][2] != ' ':
        return True
    elif board[0][0] == board[1][1] == board[2][2] != ' ':
        return True
    elif board[2][0] == board[1][1] == board[0][2] != ' ':
        return True
    else:
        return False

players = ['X', 'O']
player = []
randomPlay = random.randint(0,1)
player.append(players[randomPlay])
player.append(players[int(not randomPlay)])

print "Player 1 will play with: ", player[0]
print "Player 2 will play with: ", player[1]

initBoard()
play()