# coding=utf-8
import sys

SIZE_4_GROUPS = [
    # horizontal
    [0, 1, 2, 3],
    [4, 5, 6, 7],
    [8, 9, 10, 11],
    [12, 13, 14, 15],
    # vertical
    [0, 4, 8, 12],
    [1, 5, 9, 13],
    [2, 6, 10, 14],
    [3, 7, 11, 15],
    # box
    [0, 1, 4, 5],
    [2, 3, 6, 7],
    [8, 9, 12, 13],
    [10, 11, 14, 15]
]

SIZE_9_GROUPS = [
    # horizontal
    [0, 1, 2, 3, 4, 5, 6, 7, 8],
    [9, 10, 11, 12, 13, 14, 15, 16, 17],
    [18, 19, 20, 21, 22, 23, 24, 25, 26],
    [27, 28, 29, 30, 31, 32, 33, 34, 35],
    [36, 37, 38, 39, 40, 41, 42, 43, 44],
    [45, 46, 47, 48, 49, 50, 51, 52, 53],
    [54, 55, 56, 57, 58, 59, 60, 61, 62],
    [63, 64, 65, 66, 67, 68, 69, 70, 71],
    [72, 73, 74, 75, 76, 77, 78, 79, 80],
    # vertical
    [0, 9, 18, 27, 36, 45, 54, 63, 72],
    [1, 10, 19, 28, 37, 46, 55, 64, 73],
    [2, 11, 20, 29, 38, 47, 56, 65, 74],
    [3, 12, 21, 30, 39, 48, 57, 66, 75],
    [4, 13, 22, 31, 40, 49, 58, 67, 76],
    [5, 14, 23, 32, 41, 50, 59, 68, 77],
    [6, 15, 24, 33, 42, 51, 60, 69, 78],
    [7, 16, 25, 34, 43, 52, 61, 70, 79],
    [8, 17, 26, 35, 44, 53, 62, 71, 80],
    # box
    [0, 1, 2, 9, 10, 11, 18, 19, 20],
    [3, 4, 5, 12, 13, 14, 21, 22, 23],
    [6, 7, 8, 15, 16, 17, 24, 25, 26],
    [27, 28, 29, 36, 37, 38, 45, 46, 47],
    [30, 31, 32, 39, 40, 41, 48, 49, 50],
    [33, 34, 35, 42, 43, 44, 51, 52, 53],
    [54, 55, 56, 63, 64, 65, 72, 73, 74],
    [57, 58, 59, 66, 67, 68, 75, 76, 77],
    [60, 61, 62, 69, 70, 71, 78, 79, 80]
]


def get_groups(size):
    if size == 4:
        return SIZE_4_GROUPS
    if size == 9:
        return SIZE_9_GROUPS


def is_valid_sudoku(size, digits):
    """
    >>> is_valid_sudoku(4, [1,4,2,3,2,3,1,4,4,2,3,1,3,1,4,2])
    True
    >>> is_valid_sudoku(4, [2,1,3,2,3,2,1,4,1,4,2,3,2,3,4,1])
    False
    """
    chunks = [digits[x:x + size] for x in xrange(0, len(digits), size)]
    for chunk in chunks:
        print chunk
    groups = get_groups(size)
    elements = range(1, size + 1)

    for group in groups:
        values = [digits[idx] for idx in group]
        values.sort()
        if values != elements:
            return False
    return True


def main():
    test_cases = open(sys.argv[1], 'r')
    for test in test_cases:
        split_str = test.rstrip().split(";")
        size = int(split_str.pop(0))
        digits = [int(d) for d in split_str.pop(0).split(',')]
        print is_valid_sudoku(size, digits)

    test_cases.close()


if __name__ == "__main__":
    main()
