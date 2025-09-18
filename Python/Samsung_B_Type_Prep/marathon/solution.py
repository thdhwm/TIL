#####solution.py
# from typing import List
#
#
# def init(N: int) -> None:
#     pass
#
#
# def addRoad(K: int, mID: List[int], mSpotA: List[int], mSpotB: List[int], mLen: List[int]) -> None:
#     pass
#
#
# def removeRoad(mID: int) -> None:
#     pass
#
#
# def getLength(mSpot: int) -> int:
#     return 0
# ###################################################################################

from collections import defaultdict


def init(N: int) -> None:
    global spot_road, roads
    spot_road = defaultdict(list)
    roads = defaultdict()
    pass


def addRoad(K: int, mID: List[int], mSpotA: List[int], mSpotB: List[int], mLen: List[int]) -> None:
    for i in range(K):
        spot_road[mSpotA[i]].append(mID[i])
        spot_road[mSpotB[i]].append(mID[i])
        roads[mID[i]] = (mSpotA[i], mSpotB[i], mLen[i])
    pass


def removeRoad(mID: int) -> None:
    if mID not in roads:
        return
    temp_road = roads.pop(mID)
    spot_road[temp_road[0]].remove(mID)
    spot_road[temp_road[1]].remove(mID)
    pass


def getLength(mSpot: int) -> int:
    return_spot = defaultdict(list)
    def dfs(cur_spot : int, sum_len : int, visited : set, course : list) :
        if len(course) == 4 :
            return_spot[cur_spot].append((sum_len, course[:]))
            return

        for road_id in spot_road[cur_spot]:
            next_spot = roads[road_id][0] + roads[road_id][1] - cur_spot
            if road_id in visited or next_spot == mSpot:
                continue
            course.append(road_id)
            visited.add(road_id)
            dfs(next_spot, sum_len + roads[road_id][2], visited, course)
            course.pop()
            visited.remove(road_id)
        return


    dfs(mSpot, 0, set(), [])

    max_length = -1
    for s in return_spot : #16
        for l1, c1 in return_spot[s] : # 20
            temp_visited = set(c1)
            for l2, c2 in return_spot[s] : # 20
                if l1 + l2 <= 42195 :
                    flag = 0
                    for i in c2 :
                        if i in temp_visited:
                            flag = 1
                    if flag == 0 :
                        max_length = max(max_length, l1 + l2)
    return max_length