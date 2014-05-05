# coding=utf-8
import sys


def solve(l):
    elements = l.split(',')
    m = dict()

    for e in elements:
        v = m.setdefault(e, 0)
        m[e] = v + 1
        if m[e] > len(elements) / 2:
            return e

    return None


test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    line = test.rstrip()
    print solve(line)

test_cases.close()
