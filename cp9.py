#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Implement PKCS#7 padding
"""

blocklength = 20

pt = "YELLOW SUBMARINE"

if blocklength % len(pt) == 0:
    print "Correct length " + str(len(pt))
else:
    print "Incorrect length " + str(len(pt))
    print (blocklength % len(pt))

print (20 % 16)
