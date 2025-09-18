import sys
sys.stdin = open('input.txt')


def cart(start, total = 0):
    global min_total
    if sum(visited) == N:
        min_total = min(min_total, total + table[start][0])
        return

    for i in range(1, N):
        if visited[i] != 0:
            continue

        total += table[start][i]
        visited[i] = 1
        cart(i, total)
        visited[i] = 0
        total -= table[start][i]


T = int(input())

for test_case in range(1, T + 1):
    N = int(input())
    table = [list(map(int, input().split())) for _ in range(N)]
    min_total = 21e8
    # 1 -> 관리구역 다 돌고 -> 1

    visited = [0] * N
    visited[0] = 1
    cart(0, 0)
    print(f'#{test_case} {min_total}')
