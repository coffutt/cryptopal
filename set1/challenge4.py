#!/usr/bin/python

from challenge3 import brute_break

def find_encrypted(file):
    with open(file) as f:
        def trim(lines):
            return [i.rstrip('\n') for i in f]
        return max(map(brute_break, trim(f)), key=lambda x: x[0])[1]

if __name__ == '__main__':
    print find_encrypted('../data/4.txt')
