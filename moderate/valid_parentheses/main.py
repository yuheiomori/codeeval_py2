# coding=utf-8
import sys

PARENTHESES = {
    "(": ")",
    "{": "}",
    "[": "]"
}
OPEN_PARENTHESES = PARENTHESES.keys()
CLOSE_PARENTHESES = PARENTHESES.values()

test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    stack = []
    parentheses = test.rstrip()
    if bool(parentheses):
        is_valid = True
        for c in parentheses:
            if c in OPEN_PARENTHESES:
                stack.append(c)
                continue
            if c in CLOSE_PARENTHESES:
                if len(stack) > 0:
                    last_parentheses = stack.pop()
                    if PARENTHESES[last_parentheses] == c:
                        continue

                is_valid = False
                break
        print is_valid and len(stack) == 0

test_cases.close()
