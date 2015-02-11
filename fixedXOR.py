#!/usr/bin/python

from hex2base64 import hex2base64

def xor(a, b):
    return hex(int(a, 16) ^ int(b, 16))

if __name__ == "__main__":
    import sys
    print xor(sys.argv[1], sys.argv[2])
