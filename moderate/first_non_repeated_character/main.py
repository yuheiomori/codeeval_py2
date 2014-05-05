# coding=utf-8
import sys


def get_first_non_repeated_character(s):
    first_idx_of_non_repeated_character = map(lambda x: s.count(x), s).index(1)
    return s[first_idx_of_non_repeated_character]


if __name__ == '__main__':
    test_cases = open(sys.argv[1], 'r')
    for line in test_cases:
        print(get_first_non_repeated_character(line.rstrip()))

    test_cases.close()