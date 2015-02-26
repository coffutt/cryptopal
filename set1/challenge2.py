#!/usr/bin/python

from binascii import unhexlify

def xor(a, b):
    a, b = map(unhexlify, [a, b])
    return ''.join([hex(ord(i) ^ ord(j))[2:] for i,j in zip(a,b)])

if __name__ == "__main__":
    print xor('1c0111001f010100061a024b53535009181c', '686974207468652062756c6c277320657965')
