


a = "1c0111001f010100061a024b53535009181c"
b = "686974207468652062756c6c277320657965"


a = a.decode("hex")
b = b.decode("hex")
result = ""

for x in range(len(a)):
   result += chr(ord(a[x]) ^ ord(b[x]))

print result
print result.encode("hex")



