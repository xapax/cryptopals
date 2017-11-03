#!/usr/bin/env python
# -*- coding: utf-8 -*-

from Crypto.Cipher import AES

"""
In this challenge we could just use the crypto-module to encrypt/decrypt in cbc-mode
But that would be cheating. So instead we are going to do it semi-manually.
By first XOR the plaintext against the IV, and then encrypt the result with the key "YELLOW SUBMARINE"

On the following iteratations we will XOR the plaintext against the ciphertext from the previous block.
"""


import binascii

IV = "0" * 16
#IV = "\x00"*16
key = "YELLOW SUBMARINE"
#key = "AAAAAAASUBMARINE"



b64blob = ""
ct = open("10.txt", "r")

for line in ct:
    line = line.replace("\n", "")
    b64blob += line

b64dec = b64blob.decode("base64")

 

def chunkup(text,length):
    blocks=[text[x:x+length] for x in xrange(0,len(text),length)]
    #print len(blocks)
    return blocks

def xor_blocks(block, IV):
    res = "" 
    # XORa ett block
    for x in range(len(block)):
       res += chr(ord(block[x]) ^ ord(IV[x]))
    return res


def decrypt(ct, key):
    #blocks = list(reversed(chunkup(ct,16)))
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
print decrypt(encrypted_text, key)
