from collections import deque
import sys
sys.stdin = open('input.txt')


def gotta_catch_them_all(start, distance):
    visit = visited[:]
    q = deque([(start, distance, visit)])
    min_sum = 21e8

    while q:
        now, dist, visit_each = q.popleft()
        visit_each = visit_each[:]
        visit_each[now] = 1

        if sum(visit_each) == 9:
            if min_sum > dist:
                min_sum = dist
                continue

        for go_to in range(9):
            if locations[go_to] == (-1, -1):   # if non-existent point continue
                continue

            if visit_each[go_to] != 0:    # if visited continue
                continue

            if go_to in [5, 6, 7, 8] and visit_each[go_to - 4] == 0:    # if no pokemon yet continue
                continue

            new_dist = dist + adj_matrix[now][go_to]
            q.append((go_to, new_dist, visit_each[:]))

    return min_sum


T = int(input())

for test_case in range(1, T + 1):
    N = int(input())   # table size N * N 1 <= N <= 10
    table = [list(map(int, input().split())) for _ in range(N)]
    locations = [(-1, -1)] * 9    # start, 1~4 -> trainers, -1~-4 -> pokemons    location[i] and location[i+4] are pairs
    locations[0] = (0, 0)
    visited = [0] * 9
    visited[0] = 1

    for i in range(N):
        for j in range(N):
            if table[i][j] > 0:
                locations[table[i][j]] = (i, j)

            elif table[i][j] < 0:
                locations[-table[i][j] + 4] = (i, j)

    adj_matrix = [[-1] * 9 for _ in range(9)]    # distance between each points
    for i in range(9):
        for j in range(9):
            if locations[i] == (-1, -1) or locations[j] == (-1, -1):    # don't compare distance between non-existent
                continue

            adj_matrix[i][j] = abs(locations[i][0] - locations[j][0]) + abs(locations[i][1] - locations[j][1])

    for k in range(9):      # consider visited for non_existent points
        if locations[k] == (-1, -1):
            visited[k] = 1

    print(f'#{test_case} {gotta_catch_them_all(0, 0)}')
