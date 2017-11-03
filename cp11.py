
#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
In this challenge we need to write a program that can detect if ciphertext was create using ECB or CBC

This should be pretty easy, since the blocks in ECB will produce the same ciphertext is the same plaintext is inputed.

"""


from Crypto.Cipher import AES
import binascii
import random

IV = "0" * 16
key = "YELLOW SUBMARINE"


b64blob = ""
ct = open("10.txt", "r")

for line in ct:
    line = line.replace("\n", "")
    b64blob += line

b64dec = b64blob.decode("base64")



def random_AES_key():
   print random.random()*1000 


random_AES_key()
 
# Divide up the plaintext in chunks or arbitrary length
def chunkup(text,length):
    blocks=[text[x:x+length] for x in xrange(0,len(text),length)]
    #print len(blocks)
    return blocks

# XOR the blocks, to make it CBC-like
def xor_blocks(block, IV):
    res = "" 
    # XORa ett block
    for x in range(len(block)):
       res += chr(ord(block[x]) ^ ord(IV[x]))
    return res

# 
def decrypt(ct, key):
    blocks = chunkup(ct,16)
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

def encrypt(pt, key):
    blocks = chunkup(pt, 16)
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




"""
Implement PKCS#7 padding
"""

def padding(pt, blocklength):
    if len(pt)% blocklength != 0:
        diff = blocklength - (len(pt)%blocklength) 
        to_add = format(diff, '02')
        pt += binascii.a2b_hex(to_add)*diff
        return pt



#print decrypt(res_string, key)
pt = padding("YELLOW SUBMARINEAAAAAAAAAAAAAAAABBBBBBBBB", 16)
encrypted_text = encrypt(pt, key)
#encrypted_text = encrypt("YELLOW SUBMARINE", key)
#print encrypted_text
#print decrypt(encrypted_text, key)
