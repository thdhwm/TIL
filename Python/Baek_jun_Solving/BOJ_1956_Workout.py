import sys
sys.stdin = open('input.txt')
INF = float('inf')
answer = INF

# 플로이드 워샬로 (i 에서 j 경로) + (j 에서 i 경로) 해서 최단 싸이클 경로 구하기

# 싸이클 감지가능한 알고리즘 union-find, bellman-ford 등을 활용해서 가능?은 하겠다만..? 
# 최단 거리 사이클임을 보장 X, 비용적 타임아웃 가능성 농후
# 왜냐하면>>> 플로이드 워셜 - O(V^3)
# 벨만 포드 - O(V^2 E)   ( O(V E)를 모든 노드(V)에 대해서 해야하니까 )
# kruskal - 사이클 감지해서 '제거' 하는 알고리즘 경로를 찾는거는 도움 안될지도..?

# 이 문제 범위가 최대 V = 400, E = 160000 대충  (v*(v-1))
#V^3 쌉가능, 시간복잡도에 E들어가면 쫌...?
# 그래서 워샬 쓰자 

V, E = map(int, input().split())
matrix = [[INF] * V for _ in range(V)]    # 연결 그래프 그리고

for _ in range(E):
    a, b, c = map(int, input().split())   # 시작, 끝, 비용
    matrix[a-1][b-1] = c                  # 0 base idx

for k in range(V):
    for i in range(V):
        for j in range(V):
            if matrix[i][j] > matrix[i][k] + matrix[k][j]:    # i -> j 보다 i -> k -> j 가 더 빠르면   
                matrix[i][j] = matrix[i][k] + matrix[k][j]    # 업뎃

for i in range(V):        #  i 에서 j 찍고 i 로 오는 최단경로 찾기
    for j in range(V):
        answer = min(answer, matrix[i][j] + matrix[j][i])    

if answer == INF:         # 도착 불가능, 사이클 없음 -> -1
    print('-1')
else:                     # 가능하면 정답 출력
    print(answer)
