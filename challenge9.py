#!/usr/bin/python

def pkcs7_pad(s, block_size=16):
    pad = block_size - (len(s) % block_size)
    return s + pad*chr(pad)

if __name__ == '__main__':
    print list(pkcs7_pad('Yellow Submarine', 20))
