#!/usr/bin/python

import os
from random import randint, getrandbits as randbits
from challenge7 import aes_ecb_encrypt
from challenge8 import ecb_score
from challenge9 import pkcs7_pad
from challenge10 import aes_cbc_encrypt

def rand_bytes(length=16):
    return os.urandom(length)

def pad(data):
    return pkcs7_pad(rand_bytes(randint(5,10)) + data + rand_bytes(randint(5,10)))

def encryption_oracle(data, key=None, mode='ecb'):
    if not key:
        key = rand_bytes()
    padded = pad(data)

    if mode == 'ecb':
        print 'Using ECB'
        return aes_ecb_encrypt(padded, key)
    else:
        print 'Using CBC'
        return aes_cbc_encrypt(padded, key, rand_bytes())

def detect_encryption(oracle):
    cipher_text = oracle(chr(0) * 48)
    return 'ECB' if ecb_score(cipher_text) > 0 else 'CBC'

if __name__ == '__main__':
    for i in range(0, 10):
        print 'Detected: ' + detect_encryption(encryption_oracle)
