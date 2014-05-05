# coding=utf-8
import sys
from itertools import izip_longest


def look(pos, row):
    """
    >>> look(1, [".", "*", "."])
    1
    >>> look(2, [".", "*", "."])
    0
    >>> look(3, [".", "*", "."])
    0
    """
    mine_count = 0
    try:
        if pos >= 0 and row[pos] == '*':
            mine_count = 1
    except IndexError:
        pass
    return mine_count


def count_mines(i, j, matrix):
    row = matrix[i]
    cnt = 0
    # left
    cnt += look(j - 1, row)
    # right
    cnt += look(j + 1, row)
    # top
    if i > 0:
        above = matrix[i - 1]
        cnt += look(j - 1, above)  # top left
        cnt += look(j, above)  # top
        cnt += look(j + 1, above)  # top right
    # below
    if i < len(matrix) - 1:
        below = matrix[i + 1]
        cnt += look(j - 1, below)  # below left
        cnt += look(j, below)  # below
        cnt += look(j + 1, below)  # below right

    return cnt


def grouper(n, iterable, fillvalue=None):
    args = [iter(iterable)] * n
    return izip_longest(fillvalue=fillvalue, *args)


def main():
    test_cases = open(sys.argv[1], 'r')

    for test in test_cases:
        line = test.strip()
        if len(line) == 0:
            continue

        nums, matrix = line.split(';')
        m, n = map(lambda x: int(x), nums.split(','))
        matrix = list(matrix)
        matrix = list(grouper(n, matrix))
        for i, row in enumerate(matrix):
            for j, e in enumerate(row):
                if e == '*':
                    sys.stdout.write(e)
                else:
                    num = count_mines(i, j, matrix)
                    sys.stdout.write(str(num))
        print ""

    test_cases.close()


if __name__ == '__main__':
    main()

