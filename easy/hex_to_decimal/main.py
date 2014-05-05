# coding=utf-8
import sys

if __name__ == '__main__':
    test_cases = open(sys.argv[1], 'r')
    for line in test_cases:
        print int(line.rstrip(), 16)
    test_cases.close()
