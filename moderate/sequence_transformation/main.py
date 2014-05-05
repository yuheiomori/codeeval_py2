# coding=utf-8
import sys
import re


def compress_sequence(s):
    """
    >>> compress_sequence("AA")
    'A'
    >>> compress_sequence("AABBAA")
    'ABA'
    """
    last = s[0]
    buf = [last]
    for c in list(s):
        if c == last:
            continue
        else:
            buf.append(c)
            last = c
    return ''.join(buf)


def main():
    test_cases = open(sys.argv[1], 'r')
    for test in test_cases:
        line = test.strip()
        if len(line) == 0:
            continue

        digits, letters = line.split(' ')
        digits = compress_sequence(digits)

        patterns = []
        for d in digits:
            if d == '0':
                patterns.append("A+")
            else:
                patterns.append("[A+|B+]")

        pattern = ''.join(patterns)

        result = None
        if re.match(pattern, letters):
            result = 'Yes'
        else:
            result = 'No'
        print result, digits, letters, pattern
    test_cases.close()


if __name__ == '__main__':
    main()


