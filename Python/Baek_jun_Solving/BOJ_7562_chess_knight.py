from collections import deque
import sys
sys.stdin = open('input.txt')


T = int(input())
di = [-2, -1, 1, 2, 2, 1, -1, -2]
dj = [1, 2, 2, 1, -1, -2, -2, -1]
for test_case in range(1, T + 1):
    N = int(input())    # n*n board
    si, sj = map(int, input().split())
    ei, ej = map(int, input().split())

    visited = [[0] * N for _ in range(N)]
    visited[si][sj] = 1
    q = deque([(0, si, sj)])
    result = 0

    while q:
        moves, now_i, now_j = q.popleft()

        if now_i == ei and now_j == ej:
            result = moves
            break

        for k in range(8):
            ni = now_i + di[k]
            nj = now_j + dj[k]

            if 0 > ni or N <= ni or 0 > nj or N <= nj:
                continue

            if visited[ni][nj]:
                continue
            
            visited[ni][nj] = 1
            q.append((moves + 1, ni, nj))
    
    print(result)