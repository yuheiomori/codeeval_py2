# coding=utf-8
import sys


def detecting_cycles(l):
    while True:
        try:
            top = l.pop(0)
            pos = l.index(top)
            candidate = l[0:pos]
            sample = l[pos + 1:pos + 1 + len(candidate)]
            if candidate == sample:
                candidate.insert(0, top)
                return candidate

        except ValueError as e:
            continue
        except IndexError:
            break

if __name__ == '__main__':
    test_cases = open(sys.argv[1], 'r')
    for line in test_cases:
        cycle = detecting_cycles(line.strip().split())
        if cycle:
            print " ".join(cycle)
    test_cases.close()