# coding=utf-8
import sys
import itertools


def main():
    test_cases = open(sys.argv[1], 'r')
    for test in test_cases:
        digits = map(lambda e: int(e), test.rstrip().split(","))

        for combination in itertools.combinations(digits, 4):
            print combination

        print len([combination for combination
                   in itertools.combinations(digits, 4)
                   if sum(combination) == 0])

    test_cases.close()


if __name__ == "__main__":
    main()
