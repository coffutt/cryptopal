#!/usr/bin/python

from binascii import unhexlify
from base64 import b64encode

def hex2base64(hex):
    return b64encode(unhexlify(hex))

if __name__ == "__main__":
    import sys
    print hex2base64(sys.argv[1])
