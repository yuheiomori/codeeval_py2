import sys


def sum_of_integers(ints):
    max_ending_here = 0
    max_so_far = max_element = -sys.maxint - 1
    for x in ints:
        max_ending_here = max(0, max_ending_here + x)
        max_so_far = max(max_so_far, max_ending_here)
        max_element = max(max_element, x)

    if max_so_far != 0:
        return max_so_far
    else:
        return max_element


if __name__ == '__main__':
    test_cases = open(sys.argv[1], 'r')
    for idx, line in enumerate(test_cases):
        print sum_of_integers([int(e.strip()) for e in line.split(',')])

    test_cases.close()