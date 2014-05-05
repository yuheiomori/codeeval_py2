# coding=utf-8
import sys
import itertools


def find_lost(l):
    """aa
    >>> find_lost(['9', '8', '3', '4', '1', '5', '7', '2'])
    '6'
    >>> find_lost(['3', '2', '1'])
    '4'
    >>> find_lost(['6', '2', '1', '7', '5', '3', '11', '4', '8', '9'])
    '10'
    """
    l = sorted(l, key=lambda x: int(x))
    for i, hint in enumerate(l):
        if hint != str(i + 1):
            return str(i + 1)
    return str(len(l) + 1)


def main():
    test_cases = open(sys.argv[1], 'r')

    for test in test_cases:
        line = test.strip()

        words, hints = [e.split(' ') for e in line.split(';')]
        hints.append(find_lost(hints))

        zipped = list(itertools.izip(words, hints))
        zipped = sorted(zipped, key=lambda x: int(x[1]))
        print ' '.join([z[0] for z in zipped])
    test_cases.close()

if __name__ == '__main__':
    main()

