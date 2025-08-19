import sys
sys.stdin = open('input.txt')
#
# paper = [list(map(int, input().split())) for _ in range(10)]
# total = 0
# # 5 *5 paper 부터 1 * 1 까지 완전 탐색 하며 1 -> 0 으로
#
# for n in range(5, 0, -1):    # 5, 4, 3, 2, 1
#     cnt_papers = 0
#     is_over_5 = False
#     for i in range(10 - n + 1):
#         for j in range(10 - n + 1):
#             is_fit = True
#             if paper[i][j] == 1:
#                 for p in range(n):
#                     for q in range(n):
#                         if paper[i + p][j + q] != 1:
#                             is_fit = False
#                             break
#                     if not is_fit:
#                         break
#
#                 if is_fit:
#                     for p in range(n):
#                         for q in range(n):
#                             paper[i + p][j + q] = 0
#                     cnt_papers += 1
#                     total += 1
#                     if cnt_papers > 5:
#                         is_over_5 = True
#                         break
#                 else:
#                     break
#         if is_over_5:
#             break
#     if is_over_5:
#         break
#
# if is_over_5:
#     print(-1)
# else:
#     print(total)

# #######################################################

paper = [list(map(int, input().split())) for _ in range(10)]
cnt_list = [0] * 6    # 각 인덱스 size 5개 썻는지 확인
total = 100    # 문제 범위 밖(최대 경우 색종이 다 쓰는 25) 임의의 큰수

def is_promising(y, x, dy, dx):    # 색종이를 붙일 수 있는가 확인
    for r in range(y, dy + 1):
        for s in range(x, dx + 1):
            if paper[r][s] == 0:
                return False
    return True

def attach(y, x, dy, dx, color_paper):    # 색종이를 때고, 붙이고 표현
    for p in range(y, dy + 1):
        for q in range(x, dx + 1):
            paper[p][q] = color_paper


def dfs(how_many_papers):    # 10 * 10 범위에 대해 dfs 시작
    global total

    for i in range(10):
        for j in range(10):
            if paper[i][j] == 1:
                for k in range(5):    # 색종이 사이즈 5 ~ 1
                    di, dj = i + k, j + k
                    if cnt_list[k + 1] < 5 and di < 10 and dj < 10:

                        if is_promising(i, j ,di, dj):
                            attach(i, j ,di, dj, 0)      # 붙이기
                            cnt_list[k + 1] += 1
                            dfs(how_many_papers + 1)
                            attach(i, j ,di, dj, 1)      # 때기
                            cnt_list[k + 1] -= 1
                return

    total = min(total, how_many_papers)

dfs(0)
if total == 100:
    print(-1)
else:
    print(total)


