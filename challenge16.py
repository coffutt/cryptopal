    #!/usr/bin/python

from string import split as str_split
from challenge9 import pkcs7_pad
from challenge10 import aes_cbc_encrypt, aes_cbc_decrypt
from challenge12 import rand_bytes
from challenge15 import unpad_pkcs7

def cookie_oracle(key):
    def build_cookie(user_data):
        user_data = user_data.replace(';', '%3B').replace('=', '%3D')
        cookie_str = 'comment1=cooking%20MCs;userdata=' + user_data + ';comment2=%20like%20a%20pound%20of%20bacon'
        return aes_cbc_encrypt(pkcs7_pad(cookie_str), key)

    return build_cookie

def parse_cookie(encrypted_cookie, key):
    cookie = unpad_pkcs7(aes_cbc_decrypt(encrypted_cookie, key))
    return map(lambda x: str_split(x, '='), str_split(cookie, ';'))

def is_admin(encrypted_cookie, key):
    pairs = parse_cookie(encrypted_cookie, key)
    return next((True for k,v in pairs if k=='admin' and v == 'true'), False)

def build_admin_cookie(oracle):
    x = oracle(('A' * 16) + ':admin<true:' + ('A' * 4))
    return x[0:32] + chr(ord(x[32])^1) + x[33:38] + chr(ord(x[38])^1) + x[39:43] + chr(ord(x[43])^1) + x[44:]

if __name__ == '__main__':
    key = rand_bytes()
    oracle = cookie_oracle(key)

    admin_cookie = build_admin_cookie(oracle)

    print 'Is admin: ' + str(is_admin(admin_cookie, key))
