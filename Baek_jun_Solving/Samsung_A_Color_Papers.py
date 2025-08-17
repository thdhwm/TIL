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
# ####################################################

# paper = [list(map(int, input().split())) for _ in range(10)]
# used = [0] * 6   # 크기별 색종이 사용 개수
# answer = float('inf')
#
# def can_attach(x, y, size):
#     """(x,y)에서 size 크기 색종이를 붙일 수 있는지 확인"""
#     if x + size > 10 or y + size > 10:
#         return False
#     for i in range(size):
#         for j in range(size):
#             if paper[x+i][y+j] != 1:
#                 return False
#     return True
#
# def attach(x, y, size, val):
#     """색종이를 붙였다(0으로 덮기) or 떼기(1로 복구)"""
#     for i in range(size):
#         for j in range(size):
#             paper[x+i][y+j] = val
#
# def dfs(pos, cnt):
#     global answer
#
#     # 이미 최소값보다 많이 쓰면 중단
#     if cnt >= answer:
#         return
#
#     # pos가 100이면 (10x10 다 확인) → 답 갱신
#     if pos == 100:
#         answer = min(answer, cnt)
#         return
#
#     x, y = divmod(pos, 10)    # 몫, 나머지 튜플로 반환 (//, %)
#
#     if paper[x][y] == 0:
#         dfs(pos + 1, cnt)
#     else:
#         # 큰 색종이부터 시도
#         for size in range(5, 0, -1):
#             if used[size] == 5:
#                 continue
#             if can_attach(x, y, size):
#                 attach(x, y, size, 0)
#                 used[size] += 1
#                 dfs(pos + 1, cnt + 1)
#                 attach(x, y, size, 1)
#                 used[size] -= 1
#
# dfs(0, 0)
# print(answer if answer != float('inf') else -1)
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


