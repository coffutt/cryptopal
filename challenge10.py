#!/usr/bin/python

from challenge2 import xor
from challenge7 import aes_ecb_decrypt as ecb_decrypt

ascii_zero = '\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'

def get_blocks(data, size):
    return [data[i:i+size] for i in range(0, len(data), size)]

def aes_cbc_decrypt(cipher_text, key, iv=ascii_zero):
    blocks = get_blocks(cipher_text, len(key))
    plain_text = ''
    last_block = iv

    for block in blocks:
        plain_text += xor(ecb_decrypt(block, key), last_block)
        last_block = block

    return plain_text

if __name__ == '__main__':
    with open('./data/10.txt') as f:
        import base64
        print aes_cbc_decrypt(base64.b64decode(f.read()), 'YELLOW SUBMARINE')
