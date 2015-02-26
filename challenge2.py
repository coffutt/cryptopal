#!/usr/bin/python

from binascii import unhexlify, hexlify

def xor(a, b):
    return ''.join(map(chr, [ord(i) ^ ord(j) for i,j in zip(a,b)]))

if __name__ == "__main__":
    print hexlify(xor(*map(unhexlify, ['1c0111001f010100061a024b53535009181c', '686974207468652062756c6c277320657965'])))
