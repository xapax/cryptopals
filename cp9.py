#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Implement PKCS#7 padding
"""

import binascii
blocklength =28
pt = "YELLOW SUBMARINE"

if len(pt)% blocklength != 0:
    diff = blocklength - (len(pt)%blocklength) 
    to_add = format(diff, '02')
    pt += binascii.a2b_hex(to_add)*diff

print pt

