#!/usr/bin/python

from binascii import unhexlify

def score(s):
    char_count = len(filter(lambda x: 'a'<=x<='z' or 'A'<=x<='Z' or x==' ', s))
    return float(char_count) / len(s)

def brute_break(hexstr, ishex = True):
    leader = (0, None, None)
    decoded = unhexlify(hexstr) if ishex else hexstr
    for i in range(256):
        res = [chr(ord(s) ^ i) for s in decoded]
        t_score = score(res)
        if leader[0] < t_score:
            leader = (t_score, ''.join(res), chr(i))

    return leader

if __name__ == '__main__':
    print brute_break('1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736')[1]
