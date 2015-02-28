#!/usr/bin/python

from string import split as str_split
from challenge7 import aes_ecb_encrypt
from challenge9 import pkcs7_pad
from challenge12 import rand_bytes

def decode_cookie(cookie):
    pairs = map(lambda x: str_split(x, '='), str_split(cookie, '&'))
    return {p[0]: p[1] for p in pairs}

def encode_cookie(data):
    return reduce(lambda mem, key: mem + key + '=' + data[key] + '&', data, '')[:-1]

def gen_cookie(email):
    email = email.replace('&', '').replace('=', '')
    return encode_cookie({ 'email': email, 'uid': '10', 'role': 'user' })

def encrypt_cookie(cookie):
    key = rand_bytes()
    return (aes_ecb_encrypt(pkcs7_pad(cookie), key), key)

if __name__ == '__main__':
    encrypted, key = encrypt_cookie(gen_cookie('coffutt@udel.edu'))
