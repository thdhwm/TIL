T = int(input())

for t in range(1, T + 1):
    N, M = map(int, input().split())        # N - 행렬 N*N, M - 스프레이 범위
    base = [[0] * N for _ in range(N)]                    # 값 넣을 행렬 만듬
    for i in range(N):
        base[i] = list(map(int, input().split()))           # 행렬 설정 완료

###############################  입력 값 받기 끝  ###############################        
# 십자 모양 뿌릴 때

    genocide = 0
    
    for i in range(N):                                     # N * N 행렬에서
        for j in range(N):                             # 스프레이 중심 (i,j)
            spray_cross = 0
            spray_cross += base[i][j]                                # 중심

            for k in range (1, M):                             # 오른쪽 방향
                if (j + k) in range(N):
                    spray_cross += base[i][j + k]

            for k in range (1, M):                               # 위쪽 방향
                if (i + k) in range(N):
                    spray_cross += base[i + k][j]

            for k in range (1, M):                               # 왼쪽 방향
                if (j - k) in range(N):
                    spray_cross += base[i][j - k]

            for k in range (1, M):                             # 아래쪽 방향
                if (i - k) in range(N):
                    spray_cross += base[i - k][j]

            if spray_cross > genocide:
                genocide = spray_cross
    
# X 모양 뿌릴 때
    for i in range(N):                                     # N * N 행렬에서
        for j in range(N):                             # 스프레이 중심 (i,j)
            spray_x = 0
            spray_x += base[i][j]                                    # 중심

            for k in range (1, M):                          # 오른쪽 위 방향
                if (i - k) in range(N) and (j + k) in range(N):
                    spray_cross += base[i - k][j + k]

############################################## 아직 안바꿈  #######################
            for k in range (1, M):                        # 오른쪽 아래 방향
                if (i + k) in range(N):
                    spray_cross += base[i + k][j + k]

            for k in range (1, M):                         # 왼쪽  아래 방향
                if (j - k) in range(N):
                    spray_cross += base[i][j - k]

            for k in range (1, M):                            # 왼쪽 위 방향
                if (i - k) in range(N):
                    spray_cross += base[i - k][j]

            if spray_cross > genocide:
                genocide = spray_cross    
    








