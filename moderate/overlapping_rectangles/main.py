# coding=utf-8
import sys


class Point(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Rect(object):
    def __init__(self, p1, p2):
        self.left = min(p1.x, p2.x)
        self.right = max(p1.x, p2.x)
        self.bottom = min(p1.y, p2.y)
        self.top = max(p1.y, p2.y)

    def __str__(self):
        return "%s %s %s %s" % (self.left, self.right, self.bottom, self.top)


def solve(x1, y1, x2, y2, x3, y3, x4, y4):
    rect1 = Rect(Point(x1, y1), Point(x2, y2))
    rect2 = Rect(Point(x3, y3), Point(x4, y4))
    is_horizontal_overlap = True
    is_vertical_overlap = True
    if (rect1.left > rect2.right) or (rect1.right < rect2.left):
        is_horizontal_overlap = False
    if (rect1.top < rect2.bottom) or (rect1.bottom > rect2.top):
        is_vertical_overlap = False
    return is_horizontal_overlap and is_vertical_overlap


test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    line = test.rstrip()
    if len(line) > 0:
        print solve(*map(lambda e: int(e), line.split(",")))

test_cases.close()
