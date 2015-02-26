#!/usr/bin/python

import itertools

def ecb_score(cypher_data):
    key_len = 16
    blocks = [cypher_data[i:i+key_len] for i in range(0, len(cypher_data), key_len)]
    pairs = itertools.combinations(blocks, 2)
    return sum(map(lambda p: p[0] == p[1], pairs)) / float(len(cypher_data))

def find_ecb_cypher(cyphers):
    max_score = (0, None)

    for i in range(len(cyphers)):
        score = ecb_score(cyphers[i])
        if score > max_score[0]:
            max_score = (score, i)

    return max_score

if __name__ == '__main__':
    with open('./data/8.txt') as f:
        from binascii import unhexlify
        data = map(lambda l: unhexlify(l.rstrip()), f.readlines())

        print find_ecb_cypher(data)
