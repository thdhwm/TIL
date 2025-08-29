from heapq import heappush, heappop
import sys
sys.stdin = open('input.txt')
# 예제 BOJ 1916
# 다익스트라 -> 주어진 시작 정점에서 모든 다른 정점까지의 최단 경로를 찾는 알고리즘
# 가중치가 있는 그래프에서 최단 경로를 찾는 문제에 활용
# 음수 가중치가 있어서는 안 됨
# 동작 단계
# 1. 출발 노드 선택 - 시작 노드를 정하고, 시작 노드의 최단 경로 0으로 초기화
# 2. 우선순위 큐 활용 - 출발 노드부터 갈 수 있는 모든 경로를 우선순위 큐 (힙)에 넣음
# 3. 최단 경로 갱신 - 우선운위 큐에서 최소 비용의 노드를 꺼내서
# 해당 노드에서 갈 수 있는 모든 노드들의 최단 경로 갱신
# -> 만약 더 짧은 경로를 발견했다면 해당 노드의 최단 경로 갱신, 우선순위 큐에 추가
# 4. 목적지 도달 - 우선순위 큐에서 목적지 도달하면 해당 노드의 최단 경로 반환

n = int(input())   # 도시 개수
m = int(input())   # 버스 개수 (간선 개수)
table = [[] for _ in range(n + 1)]    # 인접 리스트 구현

for _ in range(m):
    s, e, c = map(int, input().split())    # s - 간선 시작점, e - 간선 끝점, c - 비용
    table[s].append((e, c))            # 인접 리스트 s idx 에 튜플로 (e, c) 저장

s, e = map(int, input().split())      # 찾고자 하는 경로 s 노드에서 -> e 노드까지 최단 경로


def dijkstra(s, table):      # s - 시작 노드, table - 인접 리스트  받아서
    INF = float('inf')       # 최소 비용(경로) 를 구해야 함으로 무한대(혹은 범위 밖 임의 큰수) 로 초기화
    dp = [INF] * (n + 1)     # 비용을 저장할 리스트    -> distance []  list
    dp[s] = 0                # s - 시작 노드는 이미 방문, 비용 0 으로 초기화
    q = []                   # 우선순위 큐 사용 위한 queue
    heappush(q, (0, s))    # (비용, 노드) queue 에 push -> 우선순위 큐 0 이 우선 순위, 작을수록 우선순위 up ( heap 는 뭘까? )

    while q:                   # BFS
        current_cost, current_node = heappop(q)

        if dp[current_node] < current_cost:          # 현 비용이 더 높으면 continue -> 최소비용 찾는 dijkstra 니까
            continue

        for next_node, next_cost in table[current_node]:     # 인접 리스트에서 다음 방문할 노드 찾기
            new_cost = current_cost + next_cost
            if new_cost < dp[next_node]:                    # 다음 노드 가는 비용이 이미 저장된 값보다 작으면 -> 최소면
                dp[next_node] = new_cost                    # 최소 비용 새로운 비용으로 바꾸고
                heappush(q, (new_cost, next_node))     # 다음 노드로

    return dp                                               # 최소 비용 경로 반환


result = dijkstra(s, table)                                 # 최소 비용 경로
print(result)
