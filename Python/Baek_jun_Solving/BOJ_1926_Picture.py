from collections import deque
import sys
sys.stdin = open('input.txt')


def size(r, c):
    global pic_num, max_size
    pic_size = 1
    q = deque([(r, c)])
    visited[r][c] = 1
    pic_num += 1

    while q:
        cr, cc = q.popleft()
        for k in range(4):
            nr, nc = cr + di[k], cc + dj[k]
            if 0 <= nr < n and 0 <= nc < m:
                if table[nr][nc] == 1 and visited[nr][nc] == 0:
                    pic_size += 1
                    visited[nr][nc] = pic_size
                    q.append((nr, nc))
    max_size = max(max_size, pic_size)

n, m = map(int, input().split())

table = [list(map(int, input().split())) for _ in range(n)]
visited = [[0]*m for _ in range(n)]
di = (-1, 0, 1, 0)
dj = (0, 1, 0, -1)
pic_num = 0
max_size = 0

for i in range(n):
    for j in range(m):
        if table[i][j] == 1 and visited[i][j] == 0:
            size(i, j)

print(pic_num)
print(max_size)
