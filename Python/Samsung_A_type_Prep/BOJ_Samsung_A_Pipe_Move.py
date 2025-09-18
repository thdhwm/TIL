import sys
sys.stdin = open('../Baek_jun_Solving/input.txt')


N = int(input())
table = [list(map(int, input().split())) for _ in range(N)]

dp = [[[0] * 3 for _ in range(N)] for _ in range(N)]    # [0, 0, 0] -> [세로, 가로, 대각] 방향으로 들어오는 경우의 수
dp[0][1][0] = 1      # head 가 지금 0,1 에 가로 방향으로 있음

for i in range(N):
    for j in range(N):
        if table[i][j] == 1:   # 벽이면 컨티뉴
            continue

        if j + 1 < N and table[i][j + 1] == 0:    # 벽이 아니고, 범위 안에 있으면
            dp[i][j + 1][0] += dp[i][j][0] + dp[i][j][2]
            # (i, j+1)에 가로 방향으로 들어오는 경우는
            # (i, j)에서 가로였다가 들어오는 경우와
            # (i, j)에서 대각선이였다가 들어오는 경우
        if i + 1 < N and table[i + 1][j] == 0:    # 벽이 아니고, 범위 안에 있으면
            dp[i + 1][j][1] += dp[i][j][1] + dp[i][j][2]
            # (i + 1, j)에 세로 방향으로 들어오는 경우는
            # (i, j)에서 세로였다가 들어오는 경우와
            # (i, j)에서 대각선이였다가 들어오는 경우
        if i + 1 < N and j + 1 < N and table[i][j + 1] == 0 and table[i + 1][j] == 0 and table[i + 1][j + 1] == 0:
            dp[i + 1][j + 1][2] += dp[i][j][0] + dp[i][j][1] + dp[i][j][2]
            # (i + 1, j + 1)에 대각선 방향으로 들어오는 경우는
            # (i, j)에서 가로였다가 들어오는 경우
            # (i, j)에서 세로였다가 들어오는 경우와
            # (i, j)에서 대각선이였다가 들어오는 경우

print(sum(dp[N - 1][N - 1]))


# ################################## DFS 로 구현 #################################################
# front = [0, 1]   # 파이프 머리 좌표
# rear = [0, 0]    # 파이프 꼬리 좌표
# cnt_ways = 0
# # N * N 집 1 = 벽, 파이프 시작 항상 [(0,0) (0,1)] 에서
# # #############################################
# def horizontal(tail, head):  # 가로 이동
#     if head[1] + 1 >= N or table[head[0]][head[1] + 1] == 1:
#         return
#     tail = [head[0], head[1]]
#     head = [head[0], head[1] + 1]
#     return move(tail, head)
#
# def vertical(tail, head):
#     if head[0] + 1 >= N or table[head[0] + 1][head[1]] == 1:
#         return
#     tail = [head[0], head[1]]
#     head = [head[0] + 1, head[1]]
#     return move(tail, head)
#
#
# def diagonal(tail, head):
#     if head[1] + 1 >= N or head[0] + 1 >= N:
#         return
#
#     if table[head[0] + 1][head[1] + 1] == 1 or table[head[0]][head[1] + 1] == 1 or table[head[0] + 1][head[1]] == 1:
#         return
#
#     tail = [head[0], head[1]]
#     head = [head[0] + 1, head[1] + 1]
#     return move(tail, head)
#
# def move(tail, head):    # 파이프를 다음으로 이동 시키는 함수
#     global cnt_ways
#
#     if head == [N - 1, N - 1]:    # 파이프가 끝에 도착하면 리턴
#         cnt_ways += 1
#         return
#
#
#     if head[0] == tail[0]:    # 현재 파이프가 가로인 경우
#         horizontal(tail, head)
#         diagonal(tail, head)
#
#     elif head[1] == tail[1]:    # 현재 파이프가 세로인 경우
#         vertical(tail, head)
#         diagonal(tail, head)
#
#     else:    # 현재 파이프가 대각선인 경우
#         horizontal(tail, head)
#         diagonal(tail, head)
#         vertical(tail, head)
#
# move(rear, front)
# print(cnt_ways)
#
# # ########## time out DFS -> X, DP and memoization ############## #
