from base64 import b64decode
import itertools
from challenge18 import aes_ctr_encrypt
from challenge12 import rand_bytes
from challenge17 import str_xor
from string import rstrip
from challenge3 import score_plaintext

with open('./data/19.txt') as f:
    lines = [b64decode(rstrip(l)) for l in f.readlines()]

key = b'\xa3\xc9\xe7\xedmZU\x1e\xac\x15\xe2\xaf\xb4$\xa9{'
encrypted = map(lambda i: aes_ctr_encrypt(i, key, 0), lines)

eng_chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ ,'
all_chars = map(chr, range(0,256))

possibilities = []

for indexed in map(lambda m: filter(lambda f: f != None, m), map(None,*encrypted)):
    possible_intermediates = set(all_chars)

    for i in indexed:
        i_char_intermediates = set()
        for ch in all_chars:
            intermediate = str_xor(ch, i)

            if intermediate in eng_chars:
                i_char_intermediates.add(ch)

        possible_intermediates = set.intersection(possible_intermediates, i_char_intermediates)

    possibilities.append(possible_intermediates)


# for e in encrypted:
#     c_chr = e[0]
#     possible = set()
#     for ch in all_chars:
#         transformed = chr(ord(c_chr) ^ ord(ch))
#
#         if transformed in eng_chars:
#             possible.add(ch)
#
#     possibilities.append(possible)
#
# possibilities = set.intersection(*possibilities)

possibilities = map(lambda p: {'\x00'} if len(p) == 0 else p, possibilities)
#
encrypted = encrypted[0][0:13]
possibilities = possibilities[0:13]
possibilities = itertools.product(*possibilities)
maximum = (0, None)
for p in possibilities:
    score = score_plaintext(str_xor(p, encrypted))
    if score > maximum[0]:
        maximum = (score, p)

print str_xor(p, encrypted)
