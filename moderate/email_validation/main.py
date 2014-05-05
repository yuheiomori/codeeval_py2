# coding=utf-8
import re
import sys

RE_EMAIL = re.compile(
    r"^[-\.!#$%&'*+/=?^_`{}|~0-9A-Z]+"
    r"@(?:[A-Z0-9]+(?:-*[A-Z0-9]+)*\.)+[A-Z]{2,6}$"
    , re.IGNORECASE
)


test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    test = test.strip()
    print str(bool(RE_EMAIL.search(test.strip()))).lower()


test_cases.close()
