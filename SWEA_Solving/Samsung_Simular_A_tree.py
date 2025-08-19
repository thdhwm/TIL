import sys
sys.stdin = open('input.txt')

T = int(input())
for test_case in range(1, T + 1):

    N = int(input())
    trees = list(map(int, input().split()))
    tallest = max(trees)
    days_2 = 0
    odd_days = 0
    even_days = 0
    min_days = 0
    for i in range(len(trees)):
        trees[i] = tallest - trees[i]
        if trees[i] != 0:
            trees_value = trees[i] // 3
            trees_remainders = trees[i] % 3

            days_2 += trees_value

            if trees_remainders == 1:
                odd_days += 1
            elif trees_remainders == 2:
                even_days += 1

    min_days += 2 * days_2
    if odd_days > even_days:
        min_days += odd_days * 2 - 1
    elif odd_days == even_days:
        min_days += even_days * 2
    elif even_days > odd_days:
        can_fit = (even_days // 3)
        even_days -= can_fit
        min_days += even_days * 2

    print(f'#{test_case} {min_days}')
