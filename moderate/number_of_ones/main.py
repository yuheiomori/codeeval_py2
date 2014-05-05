# coding=utf-8
import sys


def to_bin(n):
    result = ''
    while n > 0:
        result = str(n % 2) + result
        n /= 2
    return result


def number_of_ones(s):
    return to_bin(s).count("1")


if __name__ == '__main__':
    test_cases = open(sys.argv[1], 'r')
    for line in test_cases:
        print number_of_ones(int(line.rstrip()))

    test_cases.close()