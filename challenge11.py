#!/usr/bin/python

import os

def random_aes_key(length=16):
    return os.urandom(length)

if __name__ == '__main__':
    print random_aes_key()
