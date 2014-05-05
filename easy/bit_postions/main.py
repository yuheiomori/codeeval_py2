import sys
 
 
def to_bin(n):
    result = ''
    while(n > 0):
        result = str(n % 2) + result
        n /= 2
    return result
 
 
def is_same_digit_on(n, p1, p2):
    b = to_bin(n)

    if b[len(b)-p1] == b[len(b)-p2]:
        return 'true'
    else:
        return 'false'
 
 
if __name__ == '__main__':
    test_cases = open(sys.argv[1], 'r')
    for line in test_cases:
        n, p1, p2 = [int(e) for e in line.split(',')]
        print(is_same_digit_on(n, p1, p2))
 
    test_cases.close()
