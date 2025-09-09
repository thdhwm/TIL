from collections import defaultdict
from heapq import heappop, heappush

#####solution.py


def dijkstra(graph, que, limit):
	INF = float('inf')
	dist = [INF] * _N
	for q in que:
		dist[q[1]] = 0

	while que:
		current_dist, current_node = heappop(que)  # (0,0)

		if dist[current_node] < current_dist:
			continue

		for next_distance, next_node in graph[current_node]:
			new_distance = next_distance + current_dist
			if new_distance < dist[next_node]:
				if new_distance <= limit:
					dist[next_node] = new_distance
					heappush(que, (new_distance, next_node))

	return dist



def init(N, K, sBuilding, eBuilding, mDistance):
	global graph, _N
	graph = defaultdict(list)
	_N = N
	for k in range(K):
		add(sBuilding[k], eBuilding[k], mDistance[k])


def add(sBuilding, eBuilding, mDistance):
	s, e, d = sBuilding, eBuilding, mDistance
	graph[s].append((d, e))
	graph[e].append((d, s))



def calculate(M, mCoffee, P, mBakery, R):
	qCoffee = []
	qBakery = []
	INF = float('inf')
	result = INF
	for m in range(M):
		qCoffee.append((0, mCoffee[m]))
	for p in range(P):
		qBakery.append((0, mBakery[p]))

	dCoffee = dijkstra(graph, qCoffee, R)
	dBakery = dijkstra(graph, qBakery, R)
	for i in range(len(dCoffee)):
		if dBakery[i] == 0 or dCoffee[i] == 0 or dCoffee[i] == INF or dBakery[i] == INF:
			continue
		else:
			total = dBakery[i] + dCoffee[i]
			result = min(result, total)

	if result <= 2 * R:
		# print(result)
		return result
	else:
		# print(-1)
		return -1

