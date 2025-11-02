import heapq


def dijkstra(start):
    h = []
    heapq.heappush(h, (0, start))
    while h:
        cost_, node = heapq.heappop(h)
        if distances[node] < cost_:
            continue
        else:
            for c, N in graph[node]:
                dist = c + cost_
                if distances[N] > dist:
                    distances[N] = dist
                    heapq.heappush(h, (dist, N))
                    path[N] = []
                    for p in path[node]:
                        path[N].append(p)
                    path[N].append(N)


N = int(input())  # 도시의 갯수
M = int(input())  # 버스의 갯수

# 그래프 생성
graph = [[] for _ in range(N + 1)]
for _ in range(M):
    s, e, cost = map(int, input().split())
    graph[s].append([cost, e])

start, end = map(int, input().split())  # 출발 도시, 도착 도시

# 거리 초기화
INF = float('inf')
distances = [INF] * (N + 1)
distances[start] = 0

path = [[] for _ in range(N + 1)]
path[start] = [start]

dijkstra(start)
print(distances[end])
print(len(path[end]))
print(' '.join(map(str, path[end])))
