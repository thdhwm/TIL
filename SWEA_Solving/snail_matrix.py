# T = int(input())
# N = int(input())


# for t in range(1, T + 1):                       # 5*5 예시로 생각 
#     snail = [[0] * N for _ in range(N)]         # 5*5 생성
#                           # shell의 layer
#     def snail_shell(N):
#         layer = 0
#         while snail:
#             if N == 1:
#                 snail[N // 2 + 1][N // 2 + 1] = N * N
#                 return snail
        
#             elif N == 0:                                        
#                 return snail

#             else:
#                 for i in range(N):                          # [1, 2, 3, 4, 5]
#                     snail[0 + layer][i + layer] = i + 1 # 더 더해야지           

#                 for i in range(1, N):                       # 6,    [1][5]
#                     snail[i + layer][N - 1 + layer] = i  + N                # 7,    [2][5]
#                                                         # 8,    [3][5]
#                                                         # 9,    [4][5]
#                 for i in range(N - 1):
#                     snail[N - 1 - layer][N - 2 - i - layer] = 2 * N + i       # [13, 12, 11, 10, (이미있는9)]

#                 for i in range(N -2):                           #16    [1][0]
#                     snail[N -2 - i + layer][0 + layer] = 3 * N - 1 + i          #15    [2][0]
#                                                             #14    [3][0]
#                 layer += 1                                                
#                 N -= 2
        
#     print(snail_shell(N))
    

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for t in range(1, T + 1):
    N = int(input())
    def snail_shell(N):
        snail = [[0]*N for _ in range(N)]
        num = 1                             # num을 정의 해서 반복 마다 num += 1 해서 숫자 append
        layer = 0
    
        while num <= N*N:
        # 오른쪽 방향
            for i in range(layer, N - layer):
                snail[layer][i] = num
                num += 1
        # 아래 방향
            for i in range(layer + 1, N - layer):
                snail[i][N - layer - 1] = num
                num += 1
        # 왼쪽 방향
            for i in range(N - layer - 2, layer - 1, -1):
                snail[N - layer - 1][i] = num
                num += 1
        # 위 방향
            for i in range(N - layer - 2, layer, -1):
                snail[i][layer] = num
                num += 1

            layer += 1
    
        return snail
    print(f'# {t}')
    for i in range(N):
        print(' '.join(map(str, snail_shell(N)[i]))) 