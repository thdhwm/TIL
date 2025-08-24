import sys
sys.stdin = open('../SWEA_Solving/input.txt')
# fxxk it doesn't work
# odd_days 더 클때 안댐...
# 그래서 고쳤더니 50/42
# ㅑㄴㄷ구해ㅑㅌㅇ구햗ㄱ흐ㅡㅇㄹ흗개ㅜㅑ푸얗

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
    while odd_days != 0 and even_days != 0:
        odd_days -= 1
        even_days -= 1
        min_days += 2

    if odd_days != 0:
        while odd_days > 2:
            odd_days -= 3
            min_days += 2
        if odd_days == 2:
            min_days += 2

        elif odd_days == 1:
            min_days += 1

    elif even_days != 0:
        while even_days > 2:
            even_days -= 3
            min_days += 4
        if even_days == 2:
            min_days += 3
        elif even_days == 1:
            min_days += 2

    print(f'#{test_case} {min_days}')
