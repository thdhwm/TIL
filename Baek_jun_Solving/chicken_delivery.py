from collections import deque
import sys
sys.stdin = open('input.txt')

N, M = int(input().split())    # N - n*n table, M - num chicken_h
table = [[map(int, input().split())] * N]
cnt_houses = 0
chickens = deque()
# house_in_range = []
for i in range(N):
    for j in range(N):
        if table[i][j] == 1:
            cnt_houses += 1

        elif table[i][j] == 2:
            chickens.append((i, j))

