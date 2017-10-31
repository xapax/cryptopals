a = "Burning 'em, if you ain't quick and nimble\nI go crazy when I hear a cymbal"
#a = "AAAAAAAA"
b = ""
key = "ICE"


for i in xrange(0,len(a),3):
    if i + 1 > len(a):
        b += chr(ord(a[i]) ^ ord(key[0]))
        break 
    if i + 2 >= len(a):
        b += chr(ord(a[i+1]) ^ ord(key[1]))
        break
    b += chr(ord(a[i]) ^ ord(key[0]))
    b += chr(ord(a[i+1]) ^ ord(key[1]))
    b += chr(ord(a[i+2]) ^ ord(key[2]))

print b.encode("hex")
