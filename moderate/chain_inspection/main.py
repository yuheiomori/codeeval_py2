# coding=utf-8
import sys

# chain inspection
# https://www.codeeval.com/open_challenges/119/


def solve(d):
    passed_elem = set()
    elem = 'BEGIN'
    while True:
        if elem in passed_elem:
            return False
        elif elem == 'END':
            break
        elif elem not in d.keys():
            return False
        passed_elem.add(elem)
        elem = d[elem]
    return len(d) == len(passed_elem)


test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    result = solve(dict([tuple(e.split("-")) for e in test.rstrip().split(";")]))
    if result:
        print "GOOD"
    else:
        print "BAD"
test_cases.close()