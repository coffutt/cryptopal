#!/usr/bin/python

from base64 import b64decode
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

def detect_pad_size(oracle, b_size):
    i = 0
    while True:
        encrypted = oracle((i + b_size*2)*'A')
        if encrypted[b_size:b_size*2] == encrypted[b_size*2:b_size*3]:
            return b_size - i
        i += 1

def is_ecb(oracle, b_size):
    suffix_only = oracle('')
    payload = oracle(b_size*3*'A')
    return payload[b_size:b_size*2] == payload[b_size*2:b_size*3]

def break_ecb(data, oracle):
    oracle = oracle(data)
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
    data = b64decode('Um9sbGluJyBpbiBteSA1LjAKV2l0aCBteSByYWctdG9wIGRvd24gc28gbXkgaGFpciBjYW4gYmxvdwpUaGUgZ2lybGllcyBvbiBzdGFuZGJ5IHdhdmluZyBqdXN0IHRvIHNheSBoaQpEaWQgeW91IHN0b3A/IE5vLCBJIGp1c3QgZHJvdmUgYnkK')
    print break_ecb(data, ecb_oracle)
