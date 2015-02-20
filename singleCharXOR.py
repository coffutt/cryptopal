#!/usr/bin/python

from singleByteXOR import bruteBreak

def findEncrypted(file):
    winner = { 'score': 0, 'val': None }
    with open(file) as f:
        for line in f:
            c = bruteBreak(line.rstrip('\n'))
            if (c['score'] > winner['score']):
                winner = c

    return winner['val']
        # return max(f, key=lambda line: bruteBreak(line.rstrip('\n'))['score'])

if __name__ == '__main__':
    print findEncrypted('./data/4.txt')
