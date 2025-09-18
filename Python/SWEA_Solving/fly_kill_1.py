# 2001번

T = int(input())

# (N - M + 1) * (N - M + 1) 만큼 값이 나옴

for t in range(1, T + 1):
    N, M = map(int, input().split())
    base_arr = [[0] * N for _ in range(N)]            #N*N 행렬 만듬
    for i in range(N):
        base_arr[i] = list(map(int, input().split()))     # 행렬에 숫자 다 넣음
    
    hit_arr = []    #때린 값 넣을 행렬
    
    for shift_left in range(N - M + 1):
        for shift_down in range(N - M + 1):
            hit_sum = 0
            for i in range(M):
                for j in range(M):
                    hit_sum += base_arr[i + shift_left][j + shift_down]              # 0,0에서 때리면
            hit_arr.append(hit_sum)



    print(f'#{t} {max(hit_arr)}')