import heapq     # 우선순위 큐 구현
from collections import defaultdict    # 연결 리스트 만들기 위해

# MST (최소 신장 트리) - Prim’s Algorithm (프림 알고리즘)

# 프림 알고리즘은 그래프의 최소 신장 트리를 찾는 알고리즘
# 한 시작 노드로부터 MST 집합을 확장
# 우선순위 큐를 사용해 MST에 연결된 가장 작은 가중치 간선을 선택
# 노드 중심으로 동작
# 시간 복잡도는 O((V + E) log V)
# 밀집 그래프(간선 많은 그래프)에 적합

def prim(graph, start, n):
    visited = [False] * (n + 1)    # for idx based locating -> n + 1
    pq = [(0, start)]    # priority que, (cost, node)
    mst_cost = 0        # initialize

    while pq:
        w, node = heapq.heappop(pq)
        if visited[node]:    # if already visited -> continue
            continue
        visited[node] = True    # after visiting a node, change visited
        mst_cost += w           # and add cost
        for neighbor, weight in graph[node]:    # push connected nodes to priorty que
            if not visited[neighbor]:
                heapq.heappush(pq, (weight, neighbor))

    return mst_cost


graph = defaultdict(list)
graph[1] = [(2, 4), (3, 2)]    # (연결된 노드 번호, 가중치(비용, 거리, etc.))
graph[2] = [(1, 4), (3, 1), (4, 3)]
graph[3] = [(1, 2), (2, 1), (4, 5)]
graph[4] = [(2, 3), (3, 5)]

print(prim(graph, 1, 4))    # result -> 6   (MST cost -> 2 + 1 + 3)
