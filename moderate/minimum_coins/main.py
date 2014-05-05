# coding=utf-8
import sys

coin_values = [1, 3, 5]

test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    line = test.rstrip()

    value = int(line)

    total_coin_count = 0
    for coin_value in reversed(coin_values):
        coin_count = value / coin_value
        total_coin_count += coin_count
        value -= coin_count * coin_value
        if value == 0:
            break

    print total_coin_count

test_cases.close()
