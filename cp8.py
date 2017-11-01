#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Eftersom ECB mode alltid krypterar i block om 16 byte så kan vi helt enkelt gå igenom alla block och se om någon har samma ciphertext"""



with open("8.txt") as f:
    lines = [ l.decode("hex") for l in f.read().strip().split("\n") ]
for l in lines:
    blocks=set([l[x:x+16] for x in xrange(0,len(l),16)])
    if len(blocks) < 10:
        print "ECB line is: ",l.encode("hex")

fil = open("8.txt", "r")
ct = []
for line in fil:
    line = line.replace("\n", "")
    line = line.decode("hex")
    ct.append(line)


def chunker(seq, size):
    return (seq[pos:pos + size] for pos in xrange(0, len(seq), size))


def breakup(ct,keysize):
    chunkedup = []
    for group in chunker(ct, keysize):
        chunkedup.append(group)
    return chunkedup


def search_double(ct):
    for num in range(len(ct)):
        for x in range(num+1,len(ct)):
            if num+x+1 > len(ct):
                break
            if ct[num] == ct[num+x]:
                print "ECB is: "
                print "".join(ct).encode("hex")
                break

for line in ct:
    brokenup = breakup(line,16)
    search_double(brokenup)


