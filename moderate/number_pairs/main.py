# coding=utf-8
import sys
from itertools import combinations


def number_pairs(nums, x):
    return filter(lambda t: sum(t) == x, combinations(nums, 2))


def display_number_pairs(pairs):

    if pairs:
        print ';'.join(['%s,%s' % p for p in pairs])
    else:
        print 'NULL'


if __name__ == '__main__':
    test_cases = open(sys.argv[1], 'r')
    for line in test_cases:
        nums, x = line.rstrip().split(';')
        pairs = number_pairs(map(lambda x: int(x), nums.split(',')), int(x))
        display_number_pairs(pairs)

    test_cases.close()