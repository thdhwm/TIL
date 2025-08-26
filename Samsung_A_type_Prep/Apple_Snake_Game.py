import sys
sys.stdin = open('input.txt')


T = int(input())

for test_case in range(1, T + 1):
    N = int(input())
    table = [list(map(int, input().split())) for _ in range(N)]
    apples = [0] * 11                                            # 사과 위치 저장
    turns = 0                       # turns % 4 로 방향 나타냄, 동, 남, 서, 북 순서
    d_t1 = [(1, 1), (1, -1), (-1, -1), (-1, 1)]    # 각 방향 1 turn 으로 가능 경우
    d_t2 = [(1, -1), (-1, -1), (-1, 1), (1, 1)]    # 각 방향 2 turn 으로 가능 경우
    start_i, start_j = 0, 0

    for i in range(N):                                   # 사과 위치 순서대로 저장
        for j in range(N):
            if table[i][j] != 0:
                apples[table[i][j]] = (i, j)

    for apple in apples:
        if apple != 0:
            apple_i, apple_j = apple

            if d_t1[turns % 4][0] * apple_i > d_t1[turns % 4][0] * start_i and \
                    d_t1[turns % 4][1] * apple_j > d_t1[turns % 4][1] * start_j:   # 1번 턴
                turns += 1
                start_i, start_j = apple_i, apple_j

            elif d_t2[turns % 4][0] * apple_i > d_t2[turns % 4][0] * start_i and \
                    d_t2[turns % 4][1] * apple_j > d_t2[turns % 4][1] * start_j:   # 2번 턴
                turns += 2
                start_i, start_j = apple_i, apple_j

            else:     # 3번 턴
                turns += 3
                start_i, start_j = apple_i, apple_j

    print(f'#{test_case} {turns}')


