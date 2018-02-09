import base64
class Base64Cipher:
    def encrypt(self, data):
        newData = base64.encodestring(data)
        return newData

    def decrypt(self, data):
        newData = base64.decodestring(data)
        return newData
