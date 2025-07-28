# 2001번

T = int(input())
N, M = map(int, input().split())

# (N - M + 1) * (N - M + 1) 만큼 값이 나옴

for t in range(1, T + 1):
    base_arr = [[0] * N for _ in range(N)]            #N*N 행렬 만듬
    for i in range(N):
        base_arr[i] = list(map(int, input().split()))     # 행렬에 숫자 다 넣음
    
    hit_arr = [[0] * (N - M + 1) for _ in range(N - M + 1)]    #때린 값 넣을 행렬
    for i in range(M):
        for j in range(M):
            hit_sum += base_arr[i][j]
        
    hit_arr[i].append

    
    
    
    
    print(base_arr)