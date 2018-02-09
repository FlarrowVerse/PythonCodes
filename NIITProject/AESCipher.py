from Crypto.Cipher import AES
import os

class AESCipher:

    def encrypt(self, message, passphrase):

        aes = AES.new(passphrase, AES.MODE_CBC, 'This is an IV456')
        cipherText = aes.encrypt(message)
        return cipherText

    def decrypt(self, cipherText, passphrase):
        aes  = AES.new(passphrase, AES.MODE_CBC, 'This is an IV456')
        message = aes.decrypt(cipherText)
        return message

