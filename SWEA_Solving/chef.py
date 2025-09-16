import sys
sys.stdin = open('input.txt', 'r')
T = int(input())


def combination(arr, n):       # from arr, pick n elements
    result = []
    if n > len(arr):
        return result

    if n == 1:
        for i in arr:
            result.append([i])

    elif n > 1:
        for i in range(len(arr) - n + 1):
            for j in combination(arr[i + 1:], n - 1):
                result.append([arr[i]] + j)

    return result


def diff(first, second):     # get difference between two dishes
    first_comb = combination(first, 2)      # synergy pairs in first dish
    second_comb = combination(second, 2)    # synergy pairs in second dish
    first_total = 0
    second_total = 0

    for i, j in first_comb:             # total of synergies in first dish
        first_total += graph[i][j] + graph[j][i]

    for i, j in second_comb:            # total of synergies in second dish
        second_total += graph[i][j] + graph[j][i]

    difference = abs(first_total - second_total)

    return difference


for test_case in range(1, T + 1):
    N = int(input())
    graph = [list(map(int, input().split())) for _ in range(N)]
    synergy = combination([i for i in range(N)], N//2)
    # pick half of the elements in range N, other half is automatically decided
    min_diff = 21e8
    for i in range(len(synergy)//2):
        ans = diff(synergy[i], synergy[-(i + 1)])
        min_diff = min(min_diff, ans)

    print(f'#{test_case} {min_diff}')
