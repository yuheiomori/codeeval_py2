# coding=utf-8
import sys


def is_prime(n):
    """nが素数かどうかをboolで返す
    >>> is_prime(3)
    True
    >>> is_prime(8)
    False
    """
    return not any(n % i == 0 for i in range(2, n / 2 + 1))


def prime_count_between(n1, n2):
    """n1とn2の間にある素数の数を返す
    >>> prime_count_between(2, 10)
    4
    >>> prime_count_between(20, 30)
    2
    """
    return len([n for n in range(n1, n2 + 1) if is_prime(n)])


test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    print prime_count_between(*[int(c) for c in test.rstrip().split(",")])

test_cases.close()
