import sys
sys.stdin = open('input.txt')

# 자연수 N과 M이 주어졌을 때, 아래 조건을 만족하는 길이가 M인 수열을 모두 구하기
# 1부터 N까지 자연수 중에서 중복 없이 M개를 고른 수열
N, M = map(int, input().split())
visited = [False] * (N + 1)
result = []

def dfs(depth):
    if depth == M:   # M개 뽑으면 출력
        print(*result)
        return

    for i in range(1, N + 1):
        if not visited[i]:
            if len(result) == 0 or i > max(result):
                visited[i] = True
                result.append(i)
                dfs(depth + 1)
                result.pop()
                visited[i] = False

dfs(0)

