# coding=utf-8
import sys


def remove_characters(s, s2):
    return ''.join([c for c in s if c not in s2])


if __name__ == '__main__':
    test_cases = open(sys.argv[1], 'r')
    for line in test_cases:
        s, s2 = map(lambda x: x.strip(), line.split(','))
        print remove_characters(s, s2)

    test_cases.close()