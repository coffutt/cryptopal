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
        self.lines = self._read_file()
        with open('./data/17.txt') as f:
            self.lines = map(clean_line, f.readlines())

    def get_cookie(self):
        padded_line = pkcs7_pad(random.choice(self.lines))
        return aes_cbc_encrypt(padded_line, self.key, self.iv)

    def is_valid_padding(self, encrypted_cookie):
        decrypted = aes_cbc_decrypt(encrypted_cookie, self.key, self.iv)
        return unpad_pkcs7(decrypted) != False

def crack_crypto(cipher_text, oracle):
    blocks = get_blocks(oracle, 16)
    intermediate_blocks = []
    all_chrs = [chr(i) for i in range(256)]

    for block in blocks:
        intermediate = ''
        for i in range(1, 17):
            for ch in all_chrs:
                end = ''.join([i ^ c for c in intermediate])
                if oracle(rand_bytes[16-i] + ch + end):
                    intermediate = (ch ^ i) + intermediate
                    break

        intermediate_blocks.append(intermediate)



if __name__ == '__main__':
    oracle = PaddingOracle()
    print crack_crypto(oracle.get_cookie(), oracle.is_valid_padding)
