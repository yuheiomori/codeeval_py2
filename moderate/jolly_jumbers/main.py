# coding=utf-8
import sys
from itertools import tee, izip


def pairwise(iterable):
    """s -> (s0,s1), (s1,s2), (s2, s3), ...
    """
    a, b = tee(iterable)
    next(b, None)
    return izip(a, b)


def is_jolly_jumper(nums):
    n = len(nums)
    jolly_list = [abs(t2 - t1) for t1, t2 in pairwise(nums)]
    return set(jolly_list) == set(range(1, n))


if __name__ == '__main__':
    test_cases = open(sys.argv[1], 'r')
    for line in test_cases:
        if is_jolly_jumper(map(lambda x: int(x), line.rstrip().split(' '))[1:]):
            print 'Jolly'
        else:
            print 'Not jolly'

    test_cases.close()