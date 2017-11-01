from Crypto.Cipher import AES



b64blob = ""
ct = open("7.txt", "r")




for line in ct:
    line = line.replace("\n", "")
    b64blob += line


b64dec = b64blob.decode("base64")

def decrypt(ct, key):
    
    obj = AES.new(key, AES.MODE_ECB)
    print obj.decrypt(ct)

decrypt(b64dec, "YELLOW SUBMARINE")
