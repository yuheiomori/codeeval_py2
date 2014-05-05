import sys

COINS = {
    'PENNY': .01,
    'NICKEL': .05,
    'DIME': .10,
    'QUARTER': .25,
    'HALF DOLLAR': .50,
    'ONE': 1.00,
    'TWO': 2.00,
    'FIVE': 5.00,
    'TEN': 10.00,
    'TWENTY': 20.00,
    'FIFTY': 50.00,
    'ONE HUNDRED': 100.00
}


def cash_register(purchase_price, cash):
    if cash - purchase_price == 0:
        return 'ZERO'
    elif cash < purchase_price:
        return 'ERROR'
    else:
        return calculate(purchase_price, cash)


def calculate(purchase_price, cash):
    change = int(cash * 100) - int(purchase_price * 100)
    result = []

    for coin_name, coin_value in sorted(COINS.items(), key=lambda x: x[1], reverse=True):
        coin_value = int(coin_value * 100)

        if change >= coin_value:
            num = change / coin_value
            change -= coin_value * num
            [result.append(coin_name) for i in range(0, num)]

        if change == 0:
            break

    return ','.join(result)


if __name__ == '__main__':
    test_cases = open(sys.argv[1], 'r')
    for line in test_cases:
        if len(line) > 0:
            pp, cp = map(lambda x: float(x), line.rstrip().split(";"))
            print cash_register(pp, cp)

    test_cases.close()