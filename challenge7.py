#!/usr/bin/python

import base64
from Crypto.Cipher import AES

def aes_decrypt(file, key):
    with open(file) as f:
        data = base64.b64decode(f.read())

    return AES.new(key, AES.MODE_ECB).decrypt(data)

if __name__ == '__main__':
    print aes_decrypt('./data/7.txt', 'YELLOW SUBMARINE')
