# coding=utf-8
import sys

test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    line = test.rstrip()
    if len(line) == 0:
        continue

    elements = line.split(";")[1].split(",")

    m = dict()
    result = []

    for e in elements:
        if e not in m:
            m.setdefault(e, 0)
            m[e] += 1
        elif m[e] == 1:
            result.append(e)

    print ','.join(result)

test_cases.close()
