T = int(input())

for t in range(1, T + 1):
    height_A, width_A = map(int, input().split())
    apt = [[0] * width_A for _ in range(height_A)]

    for i in range(height_A):
        apt[i] = list(map(int, input().split()))

    height_B, width_B = map(int, input().split())
    black_list = [[0] * width_B for _ in range(height_B)]

    for i in range(height_B):
        black_list[i] = list(map(int, input().split()))

    black_dict = {}
    count_black_list = 0
    for i in range(height_B):
        for j in range(width_B):
            black_dict[black_list[i][j]] = 1

    for i in range(height_A):
        for j in range(width_A):
            if apt[i][j] in black_dict.keys():
                count_black_list += 1

    print(f'#{t} {count_black_list} {height_A * width_A - count_black_list}')

########################################################################################
# 강사님 코드

# T = int(input())

# for t in range(1, T + 1):
#     H, W = map(int, input().split())

#     data = [0] * 100001

#     for _ in range(H):
#         row = list(map(int, input().split()))
#         for num in row:
#             data[num] += 1    # 아파트 입력 받으면서 조회

#     blacklist_count = 0
#     BH, BW = map(int, input().split())
#     for _ in range(BH):
#         row = list(map(int, input().split()))
#         for num in row:
#             blacklist_count += data[num]
#             data[num] = 0    # 중복 방지용

#     normal_count = (H * W) - blacklist_count
#     print(f'#{t} {blacklist_count} {normal_count}')

# ####################### 위 코드는 블랙리스트에 중복 있으면 오답나옴!!! #######################
#                             # 그래서 ( # 중복 방지용 ) 추가

# T = int(input())

# for tc in range(1, T + 1):
#     H, W = map(int, input().split())

#     # 주민 수를 저장할 딕셔너리
#     dat = {}

#     for _ in range(H):
#         row = list(map(int, input().split()))
#         for num in row:
#             # num 이라는 key가 없으면 value를 1으로 생성
#             # num 이라는 key가 있다면, 기존 value 에 + 1
#             dat[num] = dat.get(num, 0) + 1

#     blacklist_count = 0

#     BH, BW = map(int, input().split())
#     for _ in range(BH):
#         row = list(map(int, input().split()))
#         for num in row:
#             if dat.get(num):
#                 blacklist_count += dat[num]
#                 dat[num] = 0  # 중복 방지용

#     normal_count = (H * W) - blacklist_count
#     print(f'#{tc} {blacklist_count} {normal_count}')

