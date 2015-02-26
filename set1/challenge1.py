#!/usr/bin/python

from binascii import unhexlify
from base64 import b64encode

def hex2base64(hex):
    return b64encode(unhexlify(hex))

if __name__ == "__main__":
    print hex2base64('49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d')
