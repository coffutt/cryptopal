#!/usr/bin/python

from base64 import b64decode
from challenge6 import guess_key_len
from challenge7 import aes_ecb_encrypt
from challenge9 import pkcs7_pad
import os

def rand_bytes(length=16):
    return os.urandom(length)

def ecb_oracle(to_decrypt):
    key = rand_bytes()
    def encrypt(data):
        return aes_ecb_encrypt(pkcs7_pad(data + to_decrypt), key)
    return encrypt

def detect_cipher_len(oracle):
    initial = len(oracle(''))
    i = 1
    while True:
        diff = len(oracle('A'*i)) - initial
        if diff > 0:
            return diff
        i+=1

def is_ecb(oracle, block_size):
    suffix_only = oracle('')
    payload = oracle(block_size*3*'A')
    return payload[block_size:block_size*2] == payload[block_size*2:block_size*3]

def break_ecb(data):
    oracle = ecb_oracle(data)
    block_size = detect_cipher_len(oracle)

    if not is_ecb(oracle, block_size):
        raise Exception('This oracle does not appear to use ECB encryption')

    characters = [chr(i) for i in range(256)]
    def next_char(known):
        if len(known) == len(data):
            return known

        b_num = len(known) / block_size
        b_start, b_end = block_number*block_size, (block_number+1)*block_size
        base_pad = 'A' * (block_size - 1 - (len(known) % block_size))

        dictionary = { oracle(base_pad+known+ch)[b_start:b_end]: ch for ch in characters }
        return next_char(known + dictionary[oracle(base_pad)[b_start:b_end]])

    return next_char('')

if __name__ == '__main__':
    data = b64decode('Um9sbGluJyBpbiBteSA1LjAKV2l0aCBteSByYWctdG9wIGRvd24gc28gbXkgaGFpciBjYW4gYmxvdwpUaGUgZ2lybGllcyBvbiBzdGFuZGJ5IHdhdmluZyBqdXN0IHRvIHNheSBoaQpEaWQgeW91IHN0b3A/IE5vLCBJIGp1c3QgZHJvdmUgYnkK')
    print break_ecb(data)
