
#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
In this challenge we need to write a program that can detect if ciphertext was create using ECB or CBC

This should be pretty easy, since the blocks in ECB will produce the same ciphertext is the same plaintext is inputed.

"""


from Crypto.Cipher import AES
import binascii
import random
from random import randint

#IV = "0" * 16
IV = str(randint(1000000000000000, 9999999999999999))


b64blob = ""
ct = open("10.txt", "r")

for line in ct:
    line = line.replace("\n", "")
    b64blob += line

b64dec = b64blob.decode("base64")


def random_AES_key():
    return str(randint(1000000000000000, 9999999999999999))

#random_AES_key()



 
# Divide up the plaintext in chunks or arbitrary length
def chunkup(text,length):
    #print text
    #print length
    blocks=[text[x:x+length] for x in xrange(0,len(text),length)]
    return blocks

# XOR the blocks, to make it CBC-like
def xor_blocks(block, IV):
    res = "" 
    # XORa ett block
    for x in range(len(block)):
       res += chr(ord(block[x]) ^ ord(IV[x]))
    return res

# 
def decrypt_CBC(ct, key):
    blocks = chunkup(ct,len(key))
    decrypted = [IV]
    counter = 0
    result = []
    for block in blocks:
        decrypted.append(block)
        obj = AES.new(key, AES.MODE_ECB)
        dec = obj.decrypt(block)
        xored = xor_blocks(dec, decrypted[counter]) 
        counter = counter + 1
        result.append(xored)
    del decrypted[0]
    return "".join(result)

def encrypt_CBC(pt, key):
    blocks = chunkup(pt, len(key))
    #print blocks
    encrypted = [IV]
    counter = 0
    for block in blocks:
        xored = xor_blocks(block, encrypted[counter]) 
        #print xored
        obj = AES.new(key, AES.MODE_ECB)
        encrypted.append(obj.encrypt(xored))
        counter = counter +1

    del encrypted[0]
    
    return "".join(encrypted)


def decrypt_ECB(ct, key):
    obj = AES.new(key, AES.MODE_ECB)
    return obj.decrypt(ct)



def encrypt_ECB(pt, key):
    print len(pt)
    obj = AES.new(key, AES.MODE_ECB)
    return obj.encrypt(pt)



"""
Implement PKCS#7 padding
"""

def padding(pt, blocklength):
    if len(pt)% blocklength != 0:
        diff = blocklength - (len(pt)%blocklength) 
        to_add = format(diff, '02')
        pt += binascii.a2b_hex(to_add)*diff
        return pt
    else:
        # THIS SHOULD BE FIXED TO ADD AN ENTIRE NEW BLOCK with 16
        return pt


def encryption_oracle(pt):
    key = random_AES_key()
    # Add 5-10 random bytes to the pt
    random_pt = "".join([chr(randint(0,255)) for x in range(0,randint(5,10))])
    pt = random_pt + pt + random_pt 
    if randint(0,1) == 0:
        print "ECB"
        return encrypt_ECB(padding(pt,len(key)),key)
    else:
        print "CBC"
        return encrypt_CBC(padding(pt,len(key)),key)

def find_mode(pct):
    ct =[pct[x:x+16] for x in xrange(0,len(pct),16)]
    for num in range(len(ct)):
        for x in range(num+1,len(ct)):
            if num+x+1 > len(ct):
                print "It is CBC"
                return
            if ct[num] == ct[num+x]:
                print "It is ECB"
                return


ciphertext = encryption_oracle("YELLOW SUBMARINEYELLOW SUBMARINEYELLOW SUBMARINEYELLOW SUBMARINEYELLOW SUBMARINEYELLOW SUBMARINEYELLOW SUBMARINEYELLOW SUBMARINE")
print ciphertext
find_mode(ciphertext)
#print decrypt(res_string, key)
#pt = padding("YELLOW SUBMARINEAAAAAAAAAAAAAAAABBBBBBBBB", 16)
#encrypted_text = encrypt(pt, key)
#encrypted_text = encrypt("YELLOW SUBMARINE", key)
#print encrypted_text
#print decrypt(encrypted_text, key)
