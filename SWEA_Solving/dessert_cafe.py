import sys
sys.stdin = open('input.txt')

T = int(input())
di = [-1, 1, 1, -1]
dj = [1, 1, -1, -1]
for test_case in range(1, T + 1):
    N = int(input())
    cafes = [list(map(int, input().split())) for _ in range(N)]
    dessert_kind = []

    for i in range(N):
        for j in range(N):
            start = cafes[i][j]


