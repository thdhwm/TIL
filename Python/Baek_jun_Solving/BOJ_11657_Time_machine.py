import sys
input = sys.stdin.readline
INF = float('inf')


def bellman_ford(start):
    dist[start] = 0

    for i in range(1, n + 1):    # n번의 라운드를 반복
        for start, end, cost in edges:     # 매 라운드마다 모든 간선을 확인

            if dist[start] != INF and dist[end] > dist[start] + cost:    # 현재 간선을 거쳐서 다른 노드로 이동하는 거리가 더 짧은 경우
                dist[end] = dist[start] + cost

                if i == n:     # n번째 라운드에서도 값이 갱신된다면 음수 순환 존재
                    return True
    return False


n, m = map(int, input().split())
edges = []
dist = [INF] * (n + 1)

for _ in range(m):
    a, b, c = map(int, input().split())
    edges.append((a, b, c))

negative_cycle = bellman_ford(1)

if negative_cycle:    # 음의 싸이클 있음
    print(-1)

else:
    for i in range(2, n + 1):
        if dist[i] == INF:    # 도달할 수 없는 경우
            print(-1)
        else:    # 도달 가능한 경우
            print(dist[i])
