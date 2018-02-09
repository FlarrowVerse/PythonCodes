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
