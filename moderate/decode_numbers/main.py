# coding=utf-8
import sys
import string

# A : 1
# B : 2
# C : 3
# ...
# Z : 26
mapping = dict([(c, str(i + 1)) for i, c in enumerate(string.ascii_uppercase)])


def solve(s):
    if not s or len(s) == 1:
        return 1

    count = 0
    char_length = 1

    while True:
        target = s[:char_length]

        if len(target) != char_length:
            break
        if int(target) > 26:
            break

        count += solve(s[char_length:])
        char_length += 1

    return count


test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    line = test.rstrip()
    print solve(line)

test_cases.close()
