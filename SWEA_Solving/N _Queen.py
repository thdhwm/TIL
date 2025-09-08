import sys
sys.stdin = open('input.txt')


def queen(now):   # (1, visited)
    global total, visited

    if now == N + 1:
        total += 1
        return

    can_place = [0] * (N + 1)
    for i in range(1, N + 1):
        if visited[i] == 0:
            continue

        can_place[i] = 1
        for k in [-1, 1]:
            ni = i + abs(now - visited[i]) * k
            if  0 <= ni <= N:
                can_place[ni] = 1


    for i in range(1, N + 1):
        if visited[i] != 0 or can_place[i] != 0:
            continue

        visited[i] = now
        queen(now + 1)
        visited[i] = 0


T = int(input())

for test_case in range(1, T + 1):
    N = int(input())
    # N * N board 에서 퀸이 서로 공격 못하는 경우의 수
    # visited 를 각 행 번호로 저장, 행 번호를 이용해 대각선 공격 경우의 수 계산 먼저하기
    visited = [0] * (N + 1)
    row = 1
    total = 0

    queen(row)
    print(f'#{test_case} {total}')