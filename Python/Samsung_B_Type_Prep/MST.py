import heapq     # 우선순위 큐 구현
from collections import defaultdict    # 연결 리스트 만들기 위해
# ###############################################################################################################
# MST (최소 신장 트리) - Kruskal’s Algorithm (크루스칼 알고리즘)

# 크루스칼은 알고리즘은 그래프의 최소 신장 트리를 찾는 알고리즘
# 간선을 오름차순으로 정렬해서 사이클을 만들지 않는 간선만 추가
# Union find 를 이용해 사이클 감지
# 간선 중심으로 동작
# 시간 복잡도는 O(E logE)
# 희소 그래프(간선 적은 그래프)에 적합


def find(parent, a):
    if parent[a] != a:
        parent[a] = find(parent, parent[a])    # 경로 압축하기
    return parent[a]


def union(parent, a, b):
    a = find(parent, a)
    b = find(parent, b)
    if a < b:               # 인덱스 더 작은 쪽을 부모로
        parent[b] = a
    else:
        parent[a] = b


def kruskal(edges, n):    # n - number of nodes
    edges.sort(key=lambda x: x[2])    # cost 기준 오름차순으로 정렬
    parent = [i for i in range(n + 1)]    # 부모 테이블 초기화
    mst_cost = 0    # 초기 비용 0

    for s, e, c in edges:
        if find(parent, s) != find(parent, e):
            union(parent, s, e)
            mst_cost += c

    return mst_cost


edges = [(1, 2, 4), (1, 3, 2), (2, 3, 1), (2, 4, 3), (3, 4, 5)]

print(kruskal(edges, 4))  # 출력: 6 (MST 비용: 2+1+3)

# ###############################################################################################################
# MST (최소 신장 트리) - Prim’s Algorithm (프림 알고리즘)

# 프림 알고리즘은 그래프의 최소 신장 트리를 찾는 알고리즘
# 한 시작 노드로부터 MST 집합을 확장
# 우선순위 큐를 사용해 MST 에 연결된 가장 작은 가중치 간선을 선택
# 노드 중심으로 동작
# 시간 복잡도는 O((V + E) log V)
# 밀집 그래프(간선 많은 그래프)에 적합

# 추가 최적화 key word -> decrease key,, fibonacci heap

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

# ###############################################################################################################
