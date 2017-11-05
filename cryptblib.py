"""
My little cryptopals lib
"""

from random import randint
def random_AES_key(size, help=False):
    if help:
        print "--- random_AES_key() takes one argument. The number of digits you want the key to be. \n--- random_AES_key(3) will return for example 372"
        return 
    start = int("1" + "0"* (size-1))
    end = int("9" + "9"* (size-1))
    return str(randint(start, end))




