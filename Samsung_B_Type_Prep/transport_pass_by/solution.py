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
	global graph, _N
	graph = defaultdict(list)
	_N = N
	for i in range(K):
		add(sCity[i], eCity[i], mLimit[i])


def add(sCity, eCity, mLimit):
	graph[sCity].append((eCity, mLimit))
	graph[eCity].append((sCity, mLimit))


def calculate(sCity, eCity, M, mStopover):
	mStopover.append(eCity)
	dist = dijkstra(graph, sCity, mStopover)
	if max([dist[idx] for idx in mStopover]) == 30005:
		return -1
	return min([dist[idx] for idx in mStopover])
