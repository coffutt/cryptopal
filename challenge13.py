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

def encrypt_cookie(cookie, key):
    return aes_ecb_encrypt(pkcs7_pad(cookie), key)

def unpad_string(padded_str):
    pad_len = ord(padded_str[-1])
    return padded_str[:-pad_len] if pad_len < 16 else padded_str

def read_cookie(encrypted_cookie, key):
    return decode_cookie(unpad(aes_ecb_decrypt(encrypted_cookie, key)))

if __name__ == '__main__':
    key = rand_bytes()
    encrypted = encrypt_cookie(gen_cookie('coffutt@udel.edu'), key)

    # use email somehow to pad the encoded string and then a similar attack
    # to the one used in challenge 12 to get an admin user
