T = int(input())

for test_case in range(T):
    N, M = map(int, input().split())
    for _ in range(M):
        _edge = input()
    print(N - 1)

# 가장 적은 *종류의* 비행기 -> 최소 간선 수
# equals to...
# MST 간선 수, which is N - 1
# 이게 되냉


