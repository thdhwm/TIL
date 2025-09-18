from collections import defaultdict
from heapq import heappush, heappop


def dijkstra(graph, start, mStopover):
	V = len(graph)
	dist = [-1] * _N
	pq = [(-30005, start)]
	while pq:
		current_dist, u = heappop(pq)
		if dist[u] != -1:
			continue
		dist[u] = -current_dist
		for v, weight in graph[u]:
			distance = min(-current_dist, weight)
			heappush(pq, (-distance, v))

	return dist


def init(N, K, sCity, eCity, mLimit):
	global graph, _N          # 연결 그래프용 defaultdict, 노드(도시) 수 _N
	graph = defaultdict(list)     # defaultdict 에 연결 그래프 구현
	_N = N                          # 노드 수 따로 받아놓기
	for i in range(K):                # 그래프 구현
		add(sCity[i], eCity[i], mLimit[i])


def add(sCity, eCity, mLimit):      # 그래프에 연결 간선 추가, 양방향 그래프니까 s-e, e-s 둘 다
	graph[sCity].append((eCity, mLimit))
	graph[eCity].append((sCity, mLimit))


def calculate(sCity, eCity, M, mStopover):    # 최대 중량 계산하기
	mStopover.append(eCity)       # mStopover - 경유지, 도착점
	dist = dijkstra(graph, sCity, mStopover)     # 다익스트라로 시작점에서 각 도시별 최대 중량 구해놓기
	if max([dist[idx] for idx in mStopover]) == 30005:     # 도착 불가능할 경우 -1
		return -1
	return min([dist[idx] for idx in mStopover])        # 가능할 경우 답 리턴
