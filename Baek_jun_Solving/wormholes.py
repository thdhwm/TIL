import sys
sys.stdin = open('input.txt')
#
#
# def bellman_ford(N, edges, start):
#     dist = [float('inf')] * (N + 1)   # idx 1-based
#     dist[start] = 0
#     # predecessor = [None] * (N + 1)    # 경로 추적
#
#     for _ in range(N - 1):
#         for s, e, t in edges:
#             if dist[s] != float('inf') and dist[s] + t < dist[e]:
#                 dist[e] = dist[s] + t
#                 # predecessor[e] = t
#
#     for s, e, t in edges:
#         if dist[s] != float('inf') and dist[s] + t < dist[e]:
#             return True  # 음의 사이클 존재
#
#     # return dist, predecessor
#     return False
#
#
# T = int(input())
#
# for test_case in range(1, T + 1):
#     N, M, W = map(int, input().split())    # nodes, edges, wormholes
#     edges = []
#     is_time_travel = 0
#
#     for _ in range(M):    # edges
#         S, E, T = map(int, input().split())  # start, end, time
#         edges.append((S, E, T))
#         edges.append((E, S, T))
#
#     for _ in range(W):    # wormholes
#         S, E, T = map(int, input().split())  # start, end, time_reduced
#         edges.append((S, E, -T))
#
#
#     result = bellman_ford(N, edges, 1)
#
#     if result:
#         print('YES')
#     else:
#         print('NO')

# ######################################################################################
# 그래프의 모든 노드와 연결된 가상의 노드 0 을 추가  ( 슈퍼 소스 노드 )
# 0 에서 시작하는 bellman_ford 한번 실행
# 음의 사이클이 있으면 True, 없으면 False 리턴

def bellman_ford(N, edges):
    # 거리 초기화
    dist = [float('inf')] * (N + 1)  # 1-based indexing
    dist[0] = 0  # 슈퍼 소스 노드

    # N번 간선 완화 (슈퍼 소스 포함)
    for _ in range(N):
        updated = False
        for s, e, t in edges:
            if dist[s] != float('inf') and dist[s] + t < dist[e]:
                dist[e] = dist[s] + t
                updated = True
        if not updated:  # 더 이상 갱신 없으면 조기 종료
            break

    # 음의 사이클 확인
    for s, e, t in edges:
        if dist[s] != float('inf') and dist[s] + t < dist[e]:
            return True  # 음의 사이클 존재

    return False  # 음의 사이클 없음


T = int(input())

for _ in range(T):
    N, M, W = map(int, input().split())  # 노드, 간선, 웜홀 수
    edges = []

    # 일반 간선 (양방향)
    for _ in range(M):
        S, E, T = map(int, input().split())
        edges.append((S, E, T))
        edges.append((E, S, T))  # 양방향 추가

    # 웜홀 (단방향, 음수 가중치)
    for _ in range(W):
        S, E, T = map(int, input().split())
        edges.append((S, E, -T))

    # 슈퍼 소스 노드에서 모든 노드로 0 가중치 간선 추가
    for i in range(1, N + 1):
        edges.append((0, i, 0))

    # 음의 사이클 확인
    if bellman_ford(N, edges):
        print("YES")
    else:
        print("NO")