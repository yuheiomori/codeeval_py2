# coding=utf-8
import sys
import re


def pangrams(s):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    s = re.sub(' ', '', s).lower()

    for c in s:
        if c in alphabet:
            alphabet = re.sub(c, '', alphabet)

    if alphabet:
        return alphabet
    else:
        return 'NULL'


if __name__ == '__main__':
    test_cases = open(sys.argv[1], 'r')
    for line in test_cases:
        print pangrams(line.rstrip())

    test_cases.close()