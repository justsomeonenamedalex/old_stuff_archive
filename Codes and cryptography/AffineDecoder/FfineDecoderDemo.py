#!/usr/bin/python

import sys
import fractions

# lowercase alphabet + digits [0..9]
ALPHABET_SIZE = 36

def encrypt_char(a, b, m, x):
    return (a*x+b)%m

def decrypt_char(a, b, m, y):
    a_inv = inverse(a, m)
    return (a_inv * (y-b))%m

def inverse(x, m):
    possible_a_inv = [a for a in range(0,ALPHABET_SIZE) 
                        if fractions.gcd(a, ALPHABET_SIZE) == 1]
    for i in possible_a_inv:
        if (x*i)%m == 1:
            return i

def encrypt(a, b, x, m):
    y = []
    for i in x:
        y.append(mapDigitToAlpha(encrypt_char(a, b, m, mapAlphaToDigit(i))))

    return ''.join(y)

def decrypt(a, b, y, m):
    x = []
    for i in y:
        x.append(mapDigitToAlpha(decrypt_char(a, b, m, mapAlphaToDigit(i))))

    return ''.join(x)

def bruteforce(argv):
    message = argv[2]
    reference = argv[3]
    possible_a = [a for a in range(0, ALPHABET_SIZE) 
                    if fractions.gcd(a, ALPHABET_SIZE) == 1]
    for a in possible_a:
        for b in range(0, ALPHABET_SIZE):
            if encrypt(a, b, reference, ALPHABET_SIZE) == message[0:len(reference)]:
                print(encrypt(a, b, reference, ALPHABET_SIZE))
                print(decrypt(a, b, message, ALPHABET_SIZE))
                return (a, b)

def mapAlphaToDigit(x):
    if str.isdigit(x):
        i = ord(x)
        if 47 < i and i < 58:
            return ord(x)-22
    elif str.isalpha(x):
        return ord(x)-97

def mapDigitToAlpha(x):
    if 0 <= x and x < 26:
        return chr(x+97)
    elif 26 <= x and x < ALPHABET_SIZE:
        return chr(x+22)

def usage(command):
    print("Usage: " + command + " {-b | -d | -e} [a] [b] [message] [reference]")
    print("Options:")
    print("-b   bruteforce. Requires message and reference, ignores a and b")
    print("-d   decrypt. Requires key pair a and b and message, ignores reference")
    print("-e   encrypt. Requires key pair a and b and message, ignores reference")

def main(argv):
    if len(argv) < 2:
        usage(argv[0])

    elif argv[1] == "-b":
        print(bruteforce(argv))

    elif argv[1] == "-d":
        a = int(argv[2])
        b = int(argv[3])
        y = argv[4]
        m = ALPHABET_SIZE
        print(decrypt(a, b, y, m))

    elif argv[1] == "-e":
        a = int(argv[2])
        b = int(argv[3])
        x = argv[4]
        m = ALPHABET_SIZE
        print(encrypt(a, b, x, m))

    else:
        usage(argv[0])


if __name__ == "__main__":
    main(sys.argv)
