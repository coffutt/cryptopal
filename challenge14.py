#!/usr/bin/python

from challenge7 import aes_ecb_encrypt
from challenge9 import pkcs7_pad
from challenge12 import break_ecb, rand_bytes

def ecb_padding_oracle(to_decrypt):
    key = rand_bytes()
    def encrypt(data):
        return aes_ecb_encrypt(pkcs7_pad(data + to_decrypt), key)
    return encrypt

if __name__ == '__main__':
    from base64 import b64decode
    data = b64decode('Um9sbGluJyBpbiBteSA1LjAKV2l0aCBteSByYWctdG9wIGRvd24gc28gbXkgaGFpciBjYW4gYmxvdwpUaGUgZ2lybGllcyBvbiBzdGFuZGJ5IHdhdmluZyBqdXN0IHRvIHNheSBoaQpEaWQgeW91IHN0b3A/IE5vLCBJIGp1c3QgZHJvdmUgYnkK')
    print break_ecb(data, ecb_padding_oracle)
