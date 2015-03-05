#!/usr/bin/python

from challenge12 import rand_bytes
from challenge18 import aes_ctr_encrypt
from challenge17 import str_xor
import itertools

english_chars = 'ACBDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz ,'
all_chrs = [chr(i) for i in range(256)]

def valid_kstream_chars(c_char):
    return filter(lambda c: str_xor(c, c_char) in english_chars, all_chrs)

def guess_key(encrypted_strs):
    valid_chars = []

    for i in range(len(max(encrypted_strs, key=len))):
        eligible = filter(lambda s: len(s) > i, encrypted_strs)
        chrs = map(lambda c: set(valid_kstream_chars(c[i])), eligible)
        valid_chars.append(set.intersection(*chrs))

    return valid_chars

if __name__ == '__main__':
    from base64 import b64decode
    from string import rstrip

    with open('./data/19.txt') as f:
        lines = [b64decode(rstrip(l)) for l in f.readlines()]

    encrypted = map(lambda i: aes_ctr_encrypt(i, rand_bytes(), 0), lines)

    import binascii
    print binascii.hexlify(''.join([e[0] for e in encrypted]))
    #
    # a = guess_key(encrypted)
    # print a
