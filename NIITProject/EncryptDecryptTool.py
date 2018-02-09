from Tkinter import *
from CaesarCipher import *
from Base64Cipher import *
from AESCipher import *

#objects
cc = CaesarCipher()
b64 = Base64Cipher()
aes = AESCipher()

root = Tk(className="/Encryption,Decryption Tool") # main window
#variables
data = StringVar()
key = StringVar()
var = StringVar()
#input data
inputLabel = Label(text = 'Input:')
inputLabel.grid(row = 0, column = 0)
inputBox = Entry(root, textvariable = data)
inputBox.grid(row = 0, column = 1)

#key/passphrase input
keyLabel = Label(text = 'Key/Passphrase:')
keyLabel.grid(row = 1, column = 0)
keyBox = Entry(root, textvariable = key)
keyBox.grid(row = 1, column = 1)

#output data
outputLabel = Label(text = 'Output:')
outputLabel.grid(row = 3, column = 0)
outputBox = Label(root)
outputBox.grid(row = 3, column = 1)

#User choice
fch = Frame(root)
chlb = Label(fch, text = 'Choice:')
chlb.grid(row = 0, column = 0)
choices = ['Caesar Cipher', 'Base64 Cipher', 'AES Encryption']
menu = OptionMenu(fch, var, *choices)
menu.grid(row = 0, column = 1)
fch.grid(row = 2, column = 0)

def encrypt():
    cipherText = ''
    text = data.get()
    option = var.get()
    if option == 'Caesar Cipher':
        k = int(key.get())
        cipherText = cc.encrypt(k, text)
        print 'Caesar',
    elif option == 'Base64 Cipher':
        cipherText = b64.encrypt(text)
        print 'B64',
    elif option == 'AES Encryption':
        passphrase = key.get()
        cipherText = aes.encrypt(text, passphrase)
        print 'AES',
    print "Encrypting"
    outputBox.config(text = cipherText)


def decrypt():
    message = ''
    text = str(data.get())
    option = var.get()
    if option == 'Caesar Cipher':
        k = int(key.get())
        message = cc.decrypt(k, text)
        print 'Caesar',
    elif option == 'Base64 Cipher':
        message = b64.decrypt(text)
        print 'B64',
    elif option == 'AES Encryption':
        passphrase = key.get()
        message = aes.decrypt(text, passphrase)
        print 'AES',
    print "Decrypting"
    outputBox.config(text = message)


#buttons
fb = Frame(root)
encrypt = Button(fb, text = 'Encrypt', command = encrypt)
encrypt.grid(row = 0, column = 0,padx = 10)
decrypt = Button(fb, text = 'Decrypt', command = decrypt)
decrypt.grid(row = 0, column = 1)
fb.grid(row = 2, column = 1)


root.mainloop()

