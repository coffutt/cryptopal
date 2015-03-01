#!/usr/bin/python

from string import split as str_split
from challenge7 import aes_ecb_encrypt, aes_ecb_decrypt
from challenge9 import pkcs7_pad
from challenge12 import rand_bytes

def decode_cookie(cookie):
    return map(lambda x: str_split(x, '='), str_split(cookie, '&'))

def encode_cookie(pairs):
    return reduce(lambda mem, p: mem + p[0] + '=' + p[1] + '&', pairs, '')[:-1]

def encrypt_cookie(cookie, key):
    return aes_ecb_encrypt(pkcs7_pad(cookie), key)

def unpad_string(padded_str):
    pad_len = ord(padded_str[-1])
    return padded_str[:-pad_len] if pad_len < 16 else padded_str

def read_cookie(encrypted_cookie, key):
    return decode_cookie(unpad_string(aes_ecb_decrypt(encrypted_cookie, key)))

def gen_cookie(email, key):
    email = email.replace('&', '').replace('=', '')
    return encrypt_cookie(encode_cookie([['email',email],['uid', '10'],['role', 'user']]), key)


if __name__ == '__main__':
    key = rand_bytes()

    real_email = gen_cookie('coff@udel.edu', key)
    hack_email = gen_cookie('coff@udel.admin' + '\x0B'*11, key)

    hacked_cookie = real_email[0:32] + hack_email[16:32]
    print read_cookie(hacked_cookie, key)
