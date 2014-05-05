import sys
import re

calc_pattern = re.compile("([a-z]+)([+-])[a-z]+")

test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    test = test.rstrip()
    if len(test) == 0:
        continue

    digit, pattern = test.split()

    lp, o = calc_pattern.match(pattern).groups()

    l = int(digit[:len(lp)])
    r = int(digit[len(lp):])

    if o == '+':
        print l + r
    elif o == '-':
        print l - r
    else:
        raise ValueError()

test_cases.close()
