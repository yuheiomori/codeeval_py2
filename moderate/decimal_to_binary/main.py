# coding=utf-8
import sys


def decimal_to_binary(n):
    if n == 0:
        return '0'
    result = ''
    while n > 0:
        result = str(n % 2) + result
        n /= 2
    return result


if __name__ == '__main__':
    test_cases = open(sys.argv[1], 'r')
    for line in test_cases:
        print(decimal_to_binary(int(line.rstrip())))

    test_cases.close()