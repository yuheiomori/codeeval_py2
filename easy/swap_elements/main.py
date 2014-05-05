import sys
test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    (items, swaps) = test.rstrip('\n').split(":")
    items = [item.strip(' ') for item in items.strip(' ').split(' ')]
    swaps = [swap.strip(' ').split('-') for swap in swaps.strip(' ').split(',')]
    for swap in swaps:
        (a, b) = [int(pos) for pos in swap]
        items[b], items[a] = items[a], items[b]
    print ' '.join(items)
 
test_cases.close()

