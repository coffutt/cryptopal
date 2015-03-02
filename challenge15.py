#!/usr/bin/python

def unpad_pkcs7(plain_text, key_length=16):
    last_char = plain_text[-1]
    expected_repeats = ord(last_char)

    if expected_repeats > key_length:
        return plain_text
    elif expected_repeats * last_char == plain_text[-expected_repeats:]:
        return plain_text[0:-expected_repeats]
    else:
        raise Exception('Invalid PKCS7 padding')

if __name__ == '__main__':
    print unpad_pkcs7("ICE ICE BABY\x04\x04\x04\x04")
    print unpad_pkcs7("ICE ICE BABY ICE")
    try:
        print unpad_pkcs7("ICE ICE BABY\x05\x05\x05\x05")
    except Exception:
        print 'Invalid padding'
    try:
        print unpad_pkcs7("ICE ICE BABY\x01\x02\x03\x04")
    except Exception:
        print 'Invalid padding'
