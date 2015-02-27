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

def encrypt_random(data):
    key = rand_bytes()
    padded = pad(data)

    if bool(randbits(1)):
        return aes_ecb_encrypt(padded, key)
    else:
        return aes_cbc_encrypt(padded, key, rand_bytes())

def encryption_oracle(cipher_text):
    return 'ECB' if ecb_score(cipher_text) > 0 else 'CBC'

if __name__ == '__main__':
    with open('./data/8.txt') as f:
        lines = f.readlines();
        for i in range(len(lines)):
            print (i, encryption_oracle(lines[i]))
    # print encryption_oracle(ecb_encrypted)
