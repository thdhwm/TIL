def recursion(s, l, r):
    global call_count
    if l >= r:
        call_count += 1
        return 1
    elif s[l] != s[r]:
        call_count += 1
        return 0
    else:
        call_count += 1
        return recursion(s, l+1, r-1)

def isPalindrome(s):
    return recursion(s, 0, len(s)-1)

T = int(input())
for _ in range(T):
    call_count = 0
    Palindrome = input()
    print(isPalindrome(Palindrome), call_count)
