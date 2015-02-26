#!/usr/bin/python

import itertools

def ecb_score(cypher_data):
    key_len = 16
    blocks = [cypher_data[i:i+key_len] for i in range(0, len(cypher_data), key_len)]
    pairs = itertools.combinations(blocks, 2)
    return sum(map(lambda p: p[0] == p[1], pairs))

def find_ecb_cyphers(cyphers):
    t_lines = [(i, ecb_score(cyphers[i-1])) for i in range(1,len(cyphers)+1)]
    return filter(lambda l: l[1] > 0, t_lines)

if __name__ == '__main__':
    with open('./data/8.txt') as f:
        from binascii import unhexlify
        data = map(lambda l: unhexlify(l.rstrip()), f.readlines())
        print find_ecb_cyphers(data)
