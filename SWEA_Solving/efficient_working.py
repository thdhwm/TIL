import sys
sys.stdin = open('input.txt')

#
# def probability(row):
#     if row == N:
#         net_percentage = 1
#         for i in range(N):
#             percentage = visited[i] / 100
#             net_percentage *= percentage
#
#         result = 100 * net_percentage
#
#         return result
#
#
#     for n in range(N):
#         if visited[n] != 0:
#             continue
#
#         if works[row][n] == 0:
#             continue
#
#         visited[n] = works[row][n]
#         probability(row + 1)
#         visited[n] = 0
#
#
# T = int(input())
#
# for test_case in range(1, T + 1):
#     N = int(input())
#     works = [list(map(int, input().split())) for _ in range(N)]
#     visited = [0] * N
#
#     ans = probability(0)
#
#     print(ans)
#  ######################################################################
# 다시 비트 연산?
# N = 16, 16! ==>> 2.~~ e13 다 보는거는 절대 안댐


def probability(depth, ans):
    global max_probability

    if depth == N:
        if max_probability < ans:
            max_probability = ans
        return

    for i in range(N):
        if visited[i]:
            continue

        visited[i] = 1
        if max_probability < ans * works[depth][i] * 0.01:
            probability(depth + 1, ans * works[depth][i] * 0.01)
        visited[i] = 0



T = int(input())

for test_case in range(1, T + 1):
    N = int(input())
    works = [list(map(int, input().split())) for _ in range(N)]
    visited = [0] * N
    max_probability = 0
    ans = 1

    probability(0, ans)
    result = max_probability * 100
    print(f'#{test_case} {result:.6f}')






# {float:.6f}

# ########
# def bak(cnt,pb):
#     global maxi
#     if cnt == N:
#         if (maxi < pb):
#             maxi = pb
#         return
#     for i in range(N):
#         if(v2[i]): continue
#         v2[i] = 1
#         if pb*lst[i][cnt]*0.01 > maxi:
#             bak(cnt+1,pb*lst[i][cnt]*0.01)
#         v2[i] = 0
# for t in range(int(input())):
#     N = int(input())
#     maxi = 0
#     # jw = [x for x in range(N)]
#     v2 = [0] * N
#     lst = []
#     for _ in range(N):
#         lst.append(list(map(int,input().split())))
#     bak(0,1)
#     print(f'#{t+1} ' + '{:.6f}'.format(maxi*100))
