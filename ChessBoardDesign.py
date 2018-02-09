import tkinter as tk

root = tk.Tk(className="/Chess Board") # main board

#board = []

colors = ['black','white']
for row in range(8):
    #board.append([])
    
    for column in range(8):
        #var = tk.StringVar()
        #board[row].append(tk.Frame(root))
        #board[row][column].config(bg=colors[(column + row) % 2], height=90, width=90)
        #board[row][column].grid(row=row, column=column)
        tk.Frame(root, bg=colors[(row+column)%2], height=90, width=90).grid(row=row, column=column)
        #fBox.config(bg=colors[(column+row)%2], height=90, width=90)
        #fBox.grid(row=row, column=column)
        

root.mainloop()
