from collections import deque
import sys
sys.stdin = open('input.txt')


def bfs(n):
    q = deque([0])
    while q:
        n = q.popleft()
        print(n, end=' ')
        for next_n in range(N):
            if table[n][next_n] != 1 or visited[next_n] == 1:
                continue

            visited[next_n] = 1
            q.append(next_n)


T = int(input())

for test_case in range(1, T + 1):
    N = int(input())
    table = [list(map(int, input().split())) for _ in range(N)]
    visited = [0] * N
    visited[0] = 1

    print(f'#{test_case}', end=' ')
    bfs(0)
    print('')
