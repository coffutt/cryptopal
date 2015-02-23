#!/usr/bin/python

from singleByteXOR import brute_break

def findEncrypted(file):
    with open(file) as f:
        def trim(lines):
            return [i.rstrip('\n') for i in f]
        return max(map(brute_break, trim(f)), key=lambda x: x[0])[1]

if __name__ == '__main__':
    print findEncrypted('./data/4.txt')
