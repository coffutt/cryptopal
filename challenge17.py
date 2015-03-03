#!/usr/bin/python

import random
import string
import base64
from challenge9 import pkcs7_pad
from challenge10 import aes_cbc_encrypt, aes_cbc_decrypt, get_blocks
from challenge12 import rand_bytes
from challenge15 import unpad_pkcs7

def clean_line(line):
    return base64.b64decode(string.rstrip(line))

class PaddingOracle():

    def __init__(self):
        self.key = rand_bytes()
        self.iv = rand_bytes()
        with open('./data/17.txt') as f:
            self.lines = map(clean_line, f.readlines())

    def get_iv(self): return self.iv

    def get_cookie(self):
        padded_line = pkcs7_pad(random.choice(self.lines))
        return aes_cbc_encrypt(padded_line, self.key, self.iv)

    def is_valid_padding(self, encrypted_cookie):
        decrypted = aes_cbc_decrypt(encrypted_cookie, self.key, self.iv)
        try:
            unpad_pkcs7(decrypted)
            return True
        except Exception:
            return False

def crack_crypto(cipher_text, oracle, iv):
    blocks = get_blocks(cipher_text, 16)
    intermediate_blocks = []
    all_chrs = [chr(i) for i in range(256)]

    for block in blocks:
        intermediate = ''
        for i in range(1, 17):
            for ch in all_chrs:
                end = ''.join([chr(i ^ ord(c)) for c in intermediate])
                if oracle(rand_bytes(16-i) + ch + end):
                    intermediate = chr((ord(ch) ^ i)) + intermediate
                    break

        intermediate_blocks.append(intermediate)

    plain_text = ''
    for i in range(len(intermediate_blocks)):
        i_block = intermediate_blocks[i]
        plain_text += ''.join([chr(ord(p[0]) ^ ord(p[1])) for p in zip(block, iv)])
        iv = blocks[i]

    return plain_text

if __name__ == '__main__':
    oracle = PaddingOracle()
    print crack_crypto(oracle.get_cookie(), oracle.is_valid_padding, oracle.get_iv())
