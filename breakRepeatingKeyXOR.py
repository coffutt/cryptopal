#!/usr/bin/python

def hammingDistance(a, b):
    xord = [ord(x)^ord(y) for x,y in zip(a,b)]
    return reduce(lambda mem, x: mem + bin(x).count('1'), xord, 0)

if __name__ == '__main__':
    print hammingDistance('this is a test', 'wokka wokka!!!')
