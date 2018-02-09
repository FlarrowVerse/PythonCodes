import tkinter as tk

root = tk.Tk() # main window
root.config(bg='grey')
def createPad():
    #dislb = tk.Label(root, text = 'You Pressed')
    #dislb.grid(row = 0)
    #outlb = tk.Label(root, bg='black', fg='green', width=12, bd=10)

    #show = tk.Label(text='Expression')
    #show.grid(row=4)
    showLb = tk.Label(root, bg='black', fg='green1', width=12, bd=10)
    showLb.grid(row = 0)
    # method to control the event of button pressing
    def pressed(event):
        #outlb.config(text = btnRef[event.widget])
        var = showLb['text']
        if btnRef[event.widget] == '':
            showLb.config(text='')
        else:
            showLb.config(text=var+str(btnRef[event.widget]))


    def evaluate():
        exp = showLb['text']
        showLb.config(text=str(eval(exp)))

    pad = tk.Frame(root) # frame to hold all buttons
    btnRef = {} # dictionary: holds the button references and index 
    btnText = ['1', '2', '3', '+', '4', '5', '6', '-', '7', '8', '9', '*', '/', '%', '0', 'C']
    for i in range(16):
        btn = tk.Button(pad, text = btnText[i])
        if btnText[i] == 'C':
            btnRef[btn] = ''
        else:
            btnRef[btn] = btnText[i]
        btn.bind("<Button-1>", pressed) # binding button callback action
        btn.config(highlightbackground='black')
        btn.grid(row = int(i/4), column = int(i%4), padx = 5, pady = 5) # placing
    equal = tk.Button(root, text='=', command=evaluate)
    equal.grid(row = 2)
    #outlb.grid(row = 1)
    pad.config(bg='grey')#, highlightbackground='black')
    pad.grid(row = 1)

    root.mainloop()

createPad()
