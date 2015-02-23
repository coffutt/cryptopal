#!/usr/bin/python

from binascii import hexlify

def repeating_key_xor(plaintext, key):
    encrypted = ''
    keylen = len(key)
    for i in range(0, len(plaintext), keylen):
        substr = plaintext[i:i+keylen]
        encrypted += ''.join(map(lambda pair: chr(ord(pair[0])^ord(pair[1])), zip(substr, key)))
    return hexlify(encrypted)

if __name__ == '__main__':
    print repeating_key_xor('Burning \'em, if you ain\'t quick and nimble\nI go crazy when I hear a cymbal', 'ICE')
