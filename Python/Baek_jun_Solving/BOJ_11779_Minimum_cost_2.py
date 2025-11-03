import heapq


def dijkstra(start):    # 다익스트라
    pq = []
    heapq.heappush(pq, (0, start))
    while pq:
        now_dist, now_node = heapq.heappop(pq)
        if distances[now_node] < now_dist:
            continue

        for next_cost, next_node in graph[now_node]:
            dist = next_cost + now_dist
            if distances[next_node] > dist:            # 갱신 가능이면
                distances[next_node] = dist            # 갱신하고
                heapq.heappush(pq, (dist, next_node))  # 푸쉬하고
                path[next_node] = []                   # next 노드 경로 초기화
                for p in path[now_node]:               # now 경로에 있는 도시들을
                    path[next_node].append(p)          # 경로로 추가해줌
                path[next_node].append(next_node)      # next_node 도 추가


N = int(input())  # 도시의 갯수
M = int(input())  # 버스의 갯수

graph = [[] for _ in range(N + 1)]
for _ in range(M):
    s, e, cost = map(int, input().split())
    graph[s].append([cost, e])

start, end = map(int, input().split())  # 출발 도시, 도착 도시

INF = float('inf')      # 짱 큰 숫자
distances = [INF] * (N + 1)    # 거리 배열
distances[start] = 0           # 시작은 0으로 초기화

path = [[] for _ in range(N + 1)]    # 경로 저장 배열
path[start] = [start]                # 시작은 시작 도시로 초기화

dijkstra(start)                      # 다익스트라 시작
print(distances[end])                # 최소 비용
print(len(path[end]))                # 경로에 포함되어있는 도시의 개수
print(' '.join(map(str, path[end]))) # 경로를 방문하는 도시 순서대로
