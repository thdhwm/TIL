import sys
sys.stdin = open('input.txt')

#
# # def find(parents, a):     # 얘는 안댐 순서가 중요?
# #     if parents[a] != a:
# #         parents[a] = find(parents, parents[a])
# #     return parents[a]
#
# def find(parents, a):
#     if a == parents[a]:
#         return a
#
#     parents[a] = find(parents, parents[a])
#     return parents[a]
#
# def union(parents, a, b):
#     parent_a = find(parents, a)
#     parent_b = find(parents, b)
#
#     if parent_a == parent_b:
#         return
#
#     if parent_b > parent_a:
#         parents[a] = parent_b
#
#     else:
#         parents[b] = parent_a
#
# def same(parents, a, b):
#     if find(parents, a) == find(parents, b):
#         ans.append('YES')
#     else:
#         ans.append('NO')
#
#
# T = int(input())
#
# for test_case in range(1, T + 1):
#     N, Q = map(int, input().split())
#     parents = [i for i in range(N + 1)]
#     ans = []
#     for _ in range(Q):
#         K, A, B = map(int, input().split())
#
#         if K == 0:
#             same(parents, A, B)
#             print(parents)
#
#         elif K == 1:
#             union(parents, A, B)
#
#     print(f'#{test_case}', *ans)
# ############################################################################################################
#

def find(x):
    if x == parents[x]:
        return x

    parents[x] = find(parents[x])
    return find(parents[x])


def union(x, y):
    rx = find(x)
    ry = find(y)

    if rx == ry:
        return

    parents[ry] = rx


T = int(input())

for test_case in range(1, T + 1):
    N, Q = map(int, input().split())
    parents = [i for i in range(N + 1)]
    ans = []

    for _ in range(Q):
        K, A, B = map(int, input().split())

        if K == 0:
            if find(A) == find(B):
                ans.append('YES')

            else:
                ans.append('NO')

        elif K == 1:
            union(A, B)

    print(f'#{test_case}', *ans)

#
#









