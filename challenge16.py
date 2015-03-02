#!/usr/bin/python

from string import split as str_split
from challenge9 import pkcs7_pad
from challenge10 import aes_cbc_encrypt, aes_cbc_decrypt
from challenge12 import rand_bytes
from challenge15 import unpad_pkcs7

def build_cookie(user_data, key):
    user_data = user_data.replace(';', '%3B').replace('=', '%3D')
    cookie_str = 'comment1=cooking%20MCs;userdata=' + user_data + ';comment2=%20like%20a%20pound%20of%20bacon'
    return aes_cbc_encrypt(pkcs7_pad(cookie_str), key)

def parse_cookie(encrypted_cookie, key):
    cookie = unpad_pkcs7(aes_cbc_decrypt(encrypted_cookie, key))
    return map(lambda x: str_split(x, '='), str_split(cookie, ';'))

def is_admin(encrypted_cookie, key):
    pairs = parse_cookie(encrypted_cookie, key)
    return next((True for k,v in pairs if k=='admin' and v == 'true'), False)

def make_admin(encrypted_cookie):
    ## Figure out how long hte prepended stuff is and then flip a bit around
    ## where my equals should be to get it turned on as admin. 

if __name__ == '__main__':
    key = rand_bytes()
    encrypted = build_cookie('admin=true', key)



    is_admin(encrypted, key)
