import sys
sys.stdin = open('input.txt')

N = int(input())
table = [list(map(int, input().split())) for _ in range(N)]
front = [0, 1]    # 파이프 머리 좌표
rear = [0, 0]    # 파이프 꼬리 좌표
cnt_ways = 0
# N * N 집 1 = 벽, 파이프 시작 항상 [(0,0) (0,1)] 에서
# #############################################
def horizontal(tail, head):  # 가로 이동
    if head[1] + 1 >= N or table[head[0]][head[1] + 1] == 1:
        return
    tail = [head[0], head[1]]
    head = [head[0], head[1] + 1]
    return move(tail, head)

def vertical(tail, head):
    if head[0] + 1 >= N or table[head[0] + 1][head[1]] == 1:
        return
    tail = [head[0], head[1]]
    head = [head[0] + 1, head[1]]
    return move(tail, head)


def diagonal(tail, head):
    if head[1] + 1 >= N or head[0] + 1 >= N:
        return

    if table[head[0] + 1][head[1] + 1] == 1 or table[head[0]][head[1] + 1] == 1 or table[head[0] + 1][head[1]] == 1:
        return

    tail = [head[0], head[1]]
    head = [head[0] + 1, head[1] + 1]
    return move(tail, head)

def move(tail, head):    # 파이프를 다음으로 이동 시키는 함수
    global cnt_ways

    if head == [N - 1, N - 1]:    # 파이프가 끝에 도착하면 리턴
        cnt_ways += 1
        return


    if head[0] == tail[0]:    # 현재 파이프가 가로인 경우
        horizontal(tail, head)
        diagonal(tail, head)

    elif head[1] == tail[1]:    # 현재 파이프가 세로인 경우
        vertical(tail, head)
        diagonal(tail, head)

    else:    # 현재 파이프가 대각선인 경우
        horizontal(tail, head)
        diagonal(tail, head)
        vertical(tail, head)

move(rear, front)
print(cnt_ways)

# ########## time out DFS -> X, DP and memoization ############## #
