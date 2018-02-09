from Tkinter import *
import tkMessageBox as mb

root = Tk(className="/Tic-Tac-Toe")

f = Frame(root)

seeds = {}
moves = {}

click = True

def checker(event):
    global click
    s = ''
    if click == True:
        s = 'X'
    else:
        s = 'O'
    btn = event.widget
    if moves[seeds[btn]] == 'OK':
        click = not click
        moves[seeds[btn]] = s
    btn.config(text=moves[seeds[btn]])
    checkResult()

def checkResult():
    winner = ''
    if moves[0] == moves[1] == moves[2] != 'OK':
        winner = moves[0]
    elif moves[3] == moves[4] == moves[5] != 'OK':
        winner = moves[3]
    elif moves[5] == moves[6] == moves[7] != 'OK':
        winner = moves[5]
    elif moves[0] == moves[3] == moves[6] != 'OK':
        winner = moves[3]
    elif moves[1] == moves[4] == moves[7] != 'OK':
        winner = moves[1]
    elif moves[2] == moves[5] == moves[8] != 'OK':
        winner = moves[2]
    elif moves[0] == moves[4] == moves[8] != 'OK':
        winner = moves[0]
    elif moves[2] == moves[4] == moves[6] != 'OK':
        winner = moves[2]
    if winner != '':
        mb.showinfo('Winner', 'Player '+winner+' has won this match')

for i in range(9):
    btn = Button(f, text=" ", font=('Times 26 bold'), height=2, width=4)
    seeds[btn]=i
    moves[i]='OK'
    btn.bind('<Button-1>', checker)
    btn.grid(row=i/3, column=i%3)

def reset():
    global click
    click = True
    for i in range(9):
        moves[i] = 'OK'
    for btn in seeds.keys():
        btn.config(text=' ')

f.grid(row=0)
resetBtn = Button(root, text="Reset", font=('Times 21 bold'), height = 2, width = 4,command=reset)
resetBtn.grid(row = 1)


root.mainloop()