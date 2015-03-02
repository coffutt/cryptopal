#!/usr/bin/python

import random
import os
from challenge7 import aes_ecb_encrypt
from challenge9 import pkcs7_pad
from challenge12 import detect_cipher_len, rand_bytes, is_ecb

def ecb_oracle(to_decrypt):
    key = rand_bytes()
    rand_pad = rand_bytes(random.randint(0, 16))
    def encrypt(data):
        return aes_ecb_encrypt(pkcs7_pad(rand_pad + data + to_decrypt), key)
    return encrypt

def detect_pad_size(oracle, b_size):
    i = 0
    while True:
        encrypted = oracle((i + b_size*2)*'A')
        if encrypted[b_size:b_size*2] == encrypted[b_size*2:b_size*3]:
            return b_size - i
        i += 1

def break_dynamic_ecb(data):
    oracle = ecb_oracle(data)

    b_size = detect_cipher_len(oracle)
    pad_size = detect_pad_size(oracle, b_size)

    if not is_ecb(oracle, b_size):
        raise Exception('This oracle does not appear to use ECB encryption')

    characters = [chr(i) for i in range(256)]
    def next_char(known):
        if len(known) == len(data):
            return known

        b_num = (len(known) / b_size) + 1
        b_start, b_end = b_num*b_size, (b_num+1)*b_size
        base_pad = 'A' * (b_size - 1 - (len(known) % b_size)) + 'A' * (b_size - pad_size)

        dictionary = { oracle(base_pad+known+ch)[b_start:b_end]: ch for ch in characters }
        return next_char(known + dictionary[oracle(base_pad)[b_start:b_end]])

    return next_char('')

if __name__ == '__main__':
    from base64 import b64decode
    data = b64decode('Um9sbGluJyBpbiBteSA1LjAKV2l0aCBteSByYWctdG9wIGRvd24gc28gbXkgaGFpciBjYW4gYmxvdwpUaGUgZ2lybGllcyBvbiBzdGFuZGJ5IHdhdmluZyBqdXN0IHRvIHNheSBoaQpEaWQgeW91IHN0b3A/IE5vLCBJIGp1c3QgZHJvdmUgYnkK')
    print break_dynamic_ecb(data)
