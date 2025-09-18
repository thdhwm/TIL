import sys
sys.stdin = open('input.txt')

T = int(input())
di = [-1, 0, 1, 0, -1, 1, 1, -1] # 앞에 4개 + 뒤에 4개 x
dj = [0, 1, 0, -1, 1, 1, -1, -1]
for t in range(1, T + 1):
    N, M = map(int, input().split())        # N - 행렬 N*N, M - 스프레이 범위
    table = [list(map(int, input().split())) for _ in range(N)]                    # 값 넣을 행렬 만듬
    max_kills = -1

    for i in range(N):
        for j in range(N):
            center = table[i][j]
            kills_cross = 0    # 십자 범위 킬
            kills_x = 0    # x 범위 킬
            for n in range(4):     # + 에 대하여
                for k in range(1, M):
                    ni = i + di[n] * k
                    nj = j + dj[n] * k
                    if 0 <= ni < N and 0 <= nj < N:
                        kills_cross += table[ni][nj]
            
            for n in range(4, 8):     # x 에 대하여
                for k in range(1, M):
                    ni = i + di[n] * k
                    nj = j + dj[n] * k
                    if 0 <= ni < N and 0 <= nj < N:
                        kills_x += table[ni][nj]

            if kills_x < kills_cross:
                kills_x, kills_cross = kills_cross, kills_x

            if max_kills < kills_x + center:
                max_kills = kills_x + center

    print(f'#{t} {max_kills}')











