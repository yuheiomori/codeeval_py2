import sys
 
 
def get_answer(n):
    count = 0
    candidate = n
 
    while True:
        count += 1
        candidate = reverse_and_add(candidate)
 
        if is_palindrome(candidate):
            return count, candidate
 
        if count == 1000:
            return None
 
 
def display_answer(answer):
    if answer:
        print "%s %s"  % answer
 
 
def reverse_and_add(n):
    return n + int(str(n)[::-1])
 
 
def is_palindrome(n):
    s = str(n)
    return s == s[::-1]
 
 
if __name__ == '__main__':
    test_cases = open(sys.argv[1], 'r')
    for line in test_cases:
        display_answer(get_answer(int(line.rstrip())))
    test_cases.close()
