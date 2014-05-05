# coding=utf-8
import sys


class Stack():
    def __init__(self):
        self.elements = []

    def pop(self):
        if len(self.elements) > 0:
            return self.elements.pop()
        return None

    def push(self, e):
        self.elements.append(e)

    def __len__(self):
        return len(self.elements)


if __name__ == '__main__':
    test_cases = open(sys.argv[1], 'r')
    for line in test_cases:
        stack = Stack()
        elements = line.rstrip().split(' ')
        for e in elements:
            stack.push(e)

        result = []
        while len(stack) > 0:
            result.append(stack.pop())
            stack.pop()

        print ' '.join(result)
    test_cases.close()
