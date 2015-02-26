#!/usr/bin/python

import base64
from Crypto.Cipher import AES

def aes_ecb_decrypt(data, key):
    return AES.new(key, AES.MODE_ECB).decrypt(data)

if __name__ == '__main__':
    with open('../data/7.txt') as f:
        data = base64.b64decode(f.read())
        print aes_ecb_decrypt(data, 'YELLOW SUBMARINE')
