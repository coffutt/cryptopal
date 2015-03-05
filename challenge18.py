#!/usr/bin/python

from challenge7 import aes_ecb_encrypt
from challenge17 import str_xor
from sys import maxint as MAX_INT
import struct

def little_endian_counter(nonce):
    count = 0
    while True:
        yield struct.pack('<QQ', nonce, count)
        count = count + 1 if count < MAX_INT else 0

def aes_ctr_decrypt(c_text, key, nonce):
    counter = little_endian_counter(nonce)
    blocks = range((len(c_text) / len(key)) + 1)
    key_stream = ''.join([aes_ecb_encrypt(next(counter), key) for i in blocks])
    return str_xor(c_text, key_stream[:len(c_text)])

def aes_ctr_encrypt(p_text, key, nonce):
    return aes_ctr_decrypt(p_text, key, nonce)

if __name__ == '__main__':
    import base64
    data = base64.b64decode('L77na/nrFsKvynd6HzOoG7GHTLXsTVu9qvY/2syLXzhPweyyMTJULu/6/kXX0KSvoOLSFQ==')

    print aes_ctr_decrypt(data, 'YELLOW SUBMARINE', 0)
    print aes_ctr_decrypt(aes_ctr_encrypt('ABCDEFG', 'YELLOW SUBMARINE', 0), 'YELLOW SUBMARINE', 0)
