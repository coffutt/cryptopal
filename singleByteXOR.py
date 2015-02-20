#!/usr/bin/python

from binascii import unhexlify

def score(s):
    charCount = len(filter(lambda x: 'a'<=x<='z' or 'A'<=x<='Z', s))
    return float(charCount) / len(s.replace('\0', ''))

def bruteBreak(hexstr):
    leader = (0, None)
    decoded = unhexlify(hexstr)

    for i in range(256):
        res = ''.join([chr(ord(s) ^ i) for s in decoded])
        tScore = score(res)
        if leader[0] < tScore:
            leader = (tScore, res)

    return { 'val': leader[1], 'score': leader[0] }

if __name__ == '__main__':
    print bruteBreak('1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736')
