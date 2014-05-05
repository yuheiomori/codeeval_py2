# coding=utf-8
import sys


if __name__ == '__main__':
    test_cases = open(sys.argv[1], 'r')
    for line in test_cases:
        elements = line.rstrip().split(' ')
        reversed_list, m = list(reversed(elements[0:-1])), int(elements[-1]) - 1

        try:
            print reversed_list[m]
        except IndexError:
            pass

    test_cases.close()
