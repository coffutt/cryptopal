#!/usr/bin/python

from singleByteXOR import bruteBreak

def compare(x, y):
    y = bruteBreak(y.rstrip('\n'))
    return x if x[0] > y[0] else y

def findEncrypted(file):
    with open(file) as f:
        return reduce(compare, f, (0, None))[1]

if __name__ == '__main__':
    print findEncrypted('./data/4.txt')
