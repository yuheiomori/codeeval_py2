# coding=utf-8
import sys


def word_chain(slist, result=None):
    """
    """
    if result is None:
        result = []

    if len(slist) == 0:
        return result
    elif len(slist) == 1:
        return slist[0]
    else:
        head, rest = slist[0], slist[1:]


    return None


def main():
    test_cases = open(sys.argv[1], 'r')
    for test in test_cases:
        line = test.strip()
        if len(line) == 0:
            continue

        print word_chain(line.split(","))

    test_cases.close()


if __name__ == "__main__":
    main()