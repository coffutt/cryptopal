#!/usr/bin/python

from challenge12 import rand_bytes
from challenge18 import aes_ctr_encrypt

def fixed_nonce_encrypt(items):
    return map(lambda i: aes_ctr_encrypt(i, rand_bytes(), 0), items)

if __name__ == '__main__':
    from base64 import b64decode
    from string import rstrip

    with open('./data/19.txt') as f:
        lines = [b64decode(rstrip(l)) for l in f.readlines()]

    encrypted = fixed_nonce_encrypt(lines)
    print encrypted
