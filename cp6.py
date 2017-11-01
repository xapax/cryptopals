#!/usr/bin/env python
# -*- coding: utf-8 -*-
import collections
import operator
#KEYSIZE = 2,40

a = "this is a test"
b = "wokka wokka!!!"
points = {
        "e": 12702,
        "t": 9056,
        "a": 8167,
        "o": 7507,
        "i": 6966,
        "n": 6749,
        "s": 6327,
        "h": 6094,
        "r": 5987,
        "d": 4253,
        "l": 4025,
        "c": 2782,
        "u": 2758,
        "m": 2406,
        "w": 2360,
        "f": 2228,
        "g": 2015,
        "y": 1974,
        "p": 1929,
        "b": 1492,
        "v": 978,
        "k": 772,
        "j": 153,
        "x": 150,
        "q": 95,
        "z": 74,
        " ": 10000,
        }



b64blob = ""
f = open("6.txt","r")
for line in f:
    line = line.replace("\n", "")
    b64blob += line


bs64dec = b64blob.decode("base64")



def ham(a,b):
    total = 0
    for x in range(len(a)):
        total += bin(ord(a[x])^ord(b[x])).count('1')
    return total


def calc_keysize(ct):
    possibles = {}
    ct = ct
    for y in ct:
        
        if len(ct) < 100:
            break

        for x in range(2,40):
            ham_length = ham(ct[0:x], ct[x:x+x]) / x

            if x in possibles:
                possibles[x] += ham_length 
            #possibles[x] += ham_length
            else: 
                possibles[x] = ham_length 
        
        ct = ct[40:]
    return min(possibles.iteritems(), key=operator.itemgetter(1))[0]



def chunker(seq, size):
    return (seq[pos:pos + size] for pos in xrange(0, len(seq), size))


def breakup(ct,keysize):
    chunkedup = []
    for group in chunker(ct, keysize):
        chunkedup.append(group)
    return chunkedup

def transpose(blocks):
    transposed = []

    
    for n in range(29):
        transblock = []
        for block in blocks:
            if len(block) < len(blocks[0]):
                break
            else:
                transblock.append(block[n])
        
        # Stor risk för misstag här - eftersom vi gör om knastecken till sträng
        string = "".join(str(x) for x in transblock)
        transposed.append(string)
    
    return transposed





def solveblock(transposed):

    # XOR:a varje tecken i ett block med samma XOR värde.
    # Göra detta för alla 123-karaktärer
    # Sedan kolla vilken av dessa som får högst poäng
    superkey = []
    for block in transposed:
        scoreboard = {}
        for char in range(0,126):
            res = ""
    
            # XORa ett block
            for x in range(len(block)):
               res += chr(ord(block[x]) ^ char)
    
            # Till low case för att kunna beräkna poäng
            res_lower = res.lower()
            pt = collections.defaultdict(int)
    
            # Räkna ihop antalet gånger som varje karaktär finns
            for c in res_lower:
                pt[c] += 1
            
            total_points = 0
                
            # Beräkna antal poäng som strängen får
            for key in pt:
                if key in points:
                    point = points[key] * pt[key]
                    total_points = total_points + point
            #print total_points 
            # Stoppa in poängen i scoreboarden
            scoreboard[char] = total_points
        superkey.append(chr(max(scoreboard.iteritems(), key=operator.itemgetter(1))[0]))
        
    print superkey
    #string = "".join(str(x) for x in transblock)
    the_key= "".join(superkey)
    print the_key

    return the_key


def decrypt(ct, key):
    #key = key.decode("hex")
    upchunkad = breakup(ct,len(key))
    pt = ""
    for block in upchunkad:
        #print len(block)
        mening = ""
        for n in range(0,len(block)):
            bokstav = chr(ord(block[n]) ^ ord(key[n]))
            mening += bokstav
        pt += mening 
    return pt


keysize = calc_keysize(bs64dec)
blocks = breakup(bs64dec, keysize)
transposed = transpose(blocks)
key = solveblock(transposed)
print decrypt(bs64dec,key)
#print key

