from Tkinter import *

#class Caesar Cipher
class CaesarCipher:
    def encrypt(self, key, data):
        newData = ""

        for char in data:
            ascii = ord(char)
            if ascii == 32:
                newData += " "
                continue
            elif ascii <= 90:
                newData += unichr(((ascii - 65) + key) % 26 + 65)
            else:
                newData += unichr(((ascii - 97) + key) % 26 + 97)

        return newData

    def decrypt(self, key, data):
        newData = ""
        for char in data:
            ascii = ord(char)
            if ascii == 32:
                newData += " "
                continue
            elif ascii <= 90:
                newData += unichr(((ascii - 65) - key) % 26 + 65)
            else:
                newData += unichr(((ascii - 97) - key) % 26 + 97)

        return newData
#class base64
import base64
class Base64Cipher:
    def encrypt(self, data):
        newData = base64.encodestring(data)
        return newData

    def decrypt(self, data):
        newData = base64.decodestring(data)
        return newData


caesar = CaesarCipher()
base64 = Base64Cipher()

data = StringVar()

root = Tk(className = "Encryption Tool")
inputLabel = Label(text = "Input")
inputText = Entry(root, textvariable = data) # to input the original data
outputLabel = Label(text = "Output")
outputText = Label(root) # to display the result

inputLabel.pack(side = LEFT)
inputText.pack()
outputLabel.pack(side = LEFT)
outputText.pack()

def select():
    op = option.get()
    if op == 'Caesar':
        execfile('CaesarCipher.py')
    else:
        execfile('Base64Cipher.py')

root = Tk(className = 'User Choice')

option = StringVar(root)

choices = ['Caesar', 'Base64']
menu = OptionMenu(root, option, *choices)
menu.pack(side = 'left', padx = 10, pady = 10)

submit = Button(root, text = 'Submit', command = select)
submit.pack()

root.mainloop()