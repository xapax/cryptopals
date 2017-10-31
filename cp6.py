#!/usr/bin/env python
# -*- coding: utf-8 -*-
import collections
import operator
#KEYSIZE = 2,40

a = "this is a test"
b = "wokka wokka!!!"
test = "this is a testwokka wokka!!!"

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
            #print "Keysize: " + str(x)
            ham_length = ham(ct[0:x], ct[x:x+x]) / x

            if x in possibles:
                possibles[x] += ham_length 
            #possibles[x] += ham_length
            else: 
                possibles[x] = ham_length 
            #print possibles
        
        ct = ct[40:]
    #for key in possibles:
        #print "KEYSIZE: " + str(key) + "   Points: " + str(possibles[key])
        #print "KEYSIZE: " + str(key) + "   Points: " + str(possibles[key])
    return min(possibles.iteritems(), key=operator.itemgetter(1))[0]

def chunker(seq, size):
    return (seq[pos:pos + size] for pos in xrange(0, len(seq), size))


def breakup(ct,keysize):
    chunkedup = []
    for group in chunker(ct, 29):
        chunkedup.append(group)
    print len(chunkedup)
    return chunkedup



keysize = calc_keysize(bs64dec)
breakup(bs64dec, keysize)
#print possibles

#print ham(a,b) 




