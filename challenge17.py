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

def str_xor(a, b):
    return ''.join([chr(ord(a) ^ ord(b)) for a,b in zip(a,b)])

all_chrs = [chr(i) for i in range(256)]

def padding_oracle():
    with open('./data/17.txt') as f:
        line = clean_line(random.choice(f.readlines()))
    key, iv = rand_bytes(), rand_bytes()

    def is_valid_padding(encrypted_cookie):
        try:
            unpad_pkcs7(aes_cbc_decrypt(encrypted_cookie, key, iv))
            return True
        except Exception:
            return False

    return (aes_cbc_encrypt(pkcs7_pad(line), key, iv), is_valid_padding, iv)

def crack_crypto(cipher_text, oracle, iv):
    def build_intermediate(c_block):
        intermediate = ''

        for i in range(1, 17):
            l_str = rand_bytes(16 - i)
            r_str = ''.join([chr(i ^ ord(c)) for c in intermediate])

            ch = filter(lambda ch: oracle(l_str + ch + r_str + c_block), all_chrs)[0]
            intermediate = chr(i ^ ord(ch)) + intermediate

        return intermediate

    c_blocks = get_blocks(cipher_text, 16)
    i_blocks = map(build_intermediate, c_blocks)

    pairs = zip([iv] + c_blocks, i_blocks)
    return reduce(lambda mem, pair: mem + str_xor(*pair), pairs, '')

if __name__ == '__main__':
    print crack_crypto(*padding_oracle())
