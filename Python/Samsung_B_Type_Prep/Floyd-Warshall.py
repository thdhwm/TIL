# Floyd - Warshall

# Dijskstra, Bellman-ford 등 그래프 순회법은 
# '한 지점'에서 '다른 특정 지점'까지의 최단 경로 구하는 알고리즘
# '모든 지점'에서 '다른 모든 지점'까지 최단 경로는?

# Floyd - Warshall 사용!
# 2차원 테이블에 최단 거리 정보 저장 -> ( 연결 리스트에 최단거리 정보 저장 )  
# dp 적인 알고리즘
# 시간 복잡도 O(N^3)
# 좀 느리긴 하냉...?

# D(a, b) a -> b 거리 일때
# D(a, b) = min( D(a, b), D(a, k) + D(k, b) )
# a -> b 와
# k 노드를 경유해서 가는 경로 (a -> k -> b)
# 둘 중에서 더 짧은 쪽을 선택
# 이를 모든 지점에 대해서 반복

# 기본 코드

INF = float('inf')

n = int(input())   # 노드의 개수
m = int(input())   # 간선의 개수

graph = [[INF] * (n + 1) for _ in range(n + 1)]    # 연결 리스트 (그래프 표현) 만들고, 무한대로 초기화

for a in range(1, n + 1):     # 자기 자신 거리 0으로 초기화
    for b in range(1, n + 1):
        if a == b:
            graph[a][b] = 0

for _ in range(m):           # 각 간선에 대한 정보를 입력받아, 그 값으로 초기화
    a, b, c = map(int, input().split())      # a -> b로 가는 비용 c
    graph[a][b] = c

for k in range(1, n + 1):    # dp 점화식 모든 점에 대해 실행
    for a in range(1, n + 1):
        for b in range(1, n + 1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

# ################################################################################################################

for a in range(1, n + 1):    # 거리 리스트 출력해보기 ( 2차원 )
    for b in range(1, n + 1):
        if graph[a][b] == INF:
            print('INFINITY', end=' ')
        else:
            print(graph[a][b], end=' ')
    print()

# #################################################################################################################

# sample input
# 4     ( n )
# 7     ( m )
# 1 2 4
# 1 4 6
# 2 1 3
# 2 3 7
# 3 1 5
# 3 4 4
# 4 3 2

# result
# 0 4 8 6 
# 3 0 7 9
# 5 9 0 4
# 7 11 2 0