# import sys
# sys.stdin = open('input.txt')

# ---->> 실행하면 input.txt 읽어와서 자동으로 입력되게


# ###### 퀵 소트 (임의의 피벗(pivot)값 설정하고 리스트 순회해서 (피벗보다 작은값) (피벗) (피벗보다 큰 값) 으로 정렬 ###### #

# array = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]
#
#
# def quick_sort(array, start, end):
#     if start >= end:
#         return
#     pivot = start  # 피벗 초기값은 첫번째 요소
#     left = start + 1
#     right = end
#
#     while left <= right:
#         # 피벗보다 큰 데이터를 찾을 때까지 반복
#         while left <= end and array[left] <= array[pivot]:
#             left += 1
#
#             # 피벗보다 작은 데이터를 찾을 때까지 반복
#         while right > start and array[right] >= array[pivot]:
#             right -= 1
#
#         if left > right:  # 엇갈렸다면 작은 right -=1 데이터와 피벗을 교체
#             array[right], array[pivot] = array[pivot], array[right]
#
#         else:  # 엇갈리지 않았다면 작은 데이터와 큰 데이터를 교체
#             array[left], array[right] = array[right], array[left]
#
#     # 분할 이후 왼쪽 부분과 오른쪽 부분에서 각각 정렬 수행
#     quick_sort(array, start, right - 1)
#     quick_sort(array, right + 1, end)
#
#
# quick_sort(array, 0, len(array) - 1)
# print(array)

# ########################################################################################################### #

# 우선순위 큐
# import heapq 조으다 .heappush, .heappop  조으다

# 유니온 파인드

# ########################################################################################################### #
# def fib(n):        # memoization ( top down )
#     if n <= 1:
#         return n
#     if memo[n]:
#         return memo[n]
#     memo[n] = fib(n-1) + fib(n-2)
#     return memo[n]
#
#
# N = 10  # change here for different value
# memo = [0] * (N + 1)
#
# print(fib(N))

# ################################################################################################
# def fib(n):        # dp ( bottom up )
#     dp = [0] * (n + 1)
#     dp[0] = 0
#     dp[1] = 1
#     for i in range(2, n + 1):
#         dp[i] = dp[i - 1] + dp[i - 2]
#     return dp[n]


# print(fib(10))

# ################################################################################################
# from heapq import heappush, heappop, heapify
#
# heap = [4, 15, 19, 11, 20, 13]
# heapify(heap)
#
# print(heap)

# heapify - sort list in heap order  -> make a list in to heap
# heappush(arr, element) - insert an element in heap order
# heappop() - pop minimum element

# ################################################################################################
# import heapq
# from collections import defaultdict
# import sys
# sys.stdin = open('input.txt')
#
#
# def dijkstra(start, table):
#     costs = [float('inf')] * (n + 1)
#     costs[start] = 0
#     q = []
#     heapq.heappush(q, (0, start))
#
#     while q:
#         current_dist, current_node = heapq.heappop(q)
#
#         if costs[current_node] < current_dist:
#             continue
#
#         for next_cost, next_node in table[current_node]:
#             new_cost = current_dist + next_cost
#             if costs[next_node] > new_cost:
#                 costs[next_node] = new_cost
#                 heapq.heappush(q, (new_cost, next_node))
#
#     return costs
#
#
# n = int(input())
# m = int(input())
# table = defaultdict(list)
#
# for _ in range(m):
#     s, e, c = map(int, input().split())
#     table[s].append((c, e))
#
# s, e = map(int, input().split())
#
# result = dijkstra(s, table)
# print(result)

# ##########################################################################################

# _hex = '000000000110100000000'
# _valid = '0001101'
#
# int(_hex[:7])
# a = bin(1110110110001011101101100010110001000110100100110111011)
# b = bin(111011)
#
#
# print(int(_hex) ^ int(_valid) == 0)
# print(~int(_valid))
# print(len('1110110110001011101101100010110001000110100100110111011'))
#
# for i in range(0, 8, 2):
#     print(i)

# ###########################################################################################
# def swap(n=0):
#     global result
#     if n == N:
#         result = max(result, int(''.join(board)))
#         return
#     memo = (n, tuple(board))
#     if memo in memoization:
#         return
#     memoization.add(memo)
#     for i in range(M - 1):
#         for j in range(i + 1, M):
#             board[i], board[j] = board[j], board[i]
#             swap(n + 1)
#             board[i], board[j] = board[j], board[i]
#
#
# T = int(input())
# for case_num in range(1, 1 + T):
#     a, b = input().split()
#     board = list(a)
#     N = int(b)
#     M = len(board)
#     result = 0
#     memoization = set()
#     swap()
#     print(f'#{case_num} {result}')

# ###########################################################################################
# from collections import defaultdict
# from heapq import heappush, heappop
# import sys
# sys.stdin = open('input.txt')
#
# N = int(input())   # 도시 개수
# M = int(input())   # 버스 개수 (간선 개수)
# graph = defaultdict(list)
#
# for _ in range(M):
#     s, e, d = map(int, input().split())
#     graph[s].append((d, e))     # 양방향이 아니야 이 라만릊댜매ㅜ햗ㄱ
#     # graph[e].append((d, s))
#
# start, end = map(int, input().split())
#
#
# def dijkstra(start, graph):
#     distance = [float('inf')] * (N + 1)   # 1~N city
#     distance[start] = 0
#     pq = [(0, start)]    # 비용, 시작
#
#     while pq:
#         current_dist, current_node = heappop(pq)
#         if distance[current_node] < current_dist:
#             continue
#
#         for next_distance, next_node in graph[current_node]:
#             new_distance = current_dist + next_distance
#             if new_distance < distance[next_node]:
#                 distance[next_node] = new_distance
#                 heappush(pq, (new_distance, next_node))
#
#     return distance
#
#
# result = dijkstra(start, graph)
# print(result)

# ##############################################################################################

#
# def find(parent, a):
#     root = a
#     while parent[root] != root:
#         root = parent[root]
#
#     while parent[a] != a:
#         next_node = parent[a]
#         parent[a] = root
#         a = next_node
#
#     return root
#
# rank = [0] * (n + 1)
# def union(parent, rank, a, b):
#     root_a = find(parent, a)
#     root_b = find(parent, b)
#     if root_a != root_b:
#         if rank[root_a] < rank[root_b]:
#             parent[root_a] = root_b
#
#         elif rank[root_a] > rank[root_b]:
#             parent[root_b] = root_a
#         else:
#             parent[root_b] = root_a
#             rank[root_a] += 1
#     return
#
#
# parent = []
#

# ########################################################################################
# sort 연습

# arr = [4, 3, 2, 8, 10]
# .sort(), sorted()   ->    sort 는 반환값 없고, sorted 는 정렬한 (*중요*) 새로운 (*중요*) list 반환
# sorted(arr) -> [2, 3, 4, 8, 10]   but arr 은 그대로!!!

# 특정 조건이 존재할 때, 정렬 조건을 (key) 에 넣어주어야 한다.
# lambda: 익명 함수 (일회용 함수)
# - 파라미터, return 값
# - 앞 x(파라미터): 원본 배열의 값 하나하나
# - 뒤 x(return 값): 정렬 기준
#
# # 예시 1. 짝수 우선 정렬
# arr = [4, 3, 7, 1, 2, 5, 8, 10]
# arr.sort(key=lambda x: x % 2)
# print(arr)      # [4, 2, 8, 10, 3, 7, 1, 5]
#
# # 예시 2. 짝수 우선 정렬 + 오름차순
# arr.sort(key=lambda x: (x % 2, x))   # 앞 기준( x % 2 ) 우선 정렬 후, 뒤에 있는 기준( x )으로 정렬
# print(arr)      # [2, 4, 8, 10, 1, 3, 5, 7]

# ######################################################################


def clean(row, column, facing):
    global cnt_cleaned

    while True:
        # 1. 현재 칸 청소
        if room[row][column] == 0:
            room[row][column] = 2  # 청소 완료
            cnt_cleaned += 1

        # 2. 주변 4칸 확인
        is_done = True
        for k in range(4):
            next_facing = (facing - k - 1) % 4  # 반시계 방향 회전
            ni = row + di[next_facing]
            nj = column + dj[next_facing]
            if 0 <= ni < N and 0 <= nj < M and room[ni][nj] == 0:
                is_done = False
                break

        # 3. 청소 가능한 칸이 없는 경우
        if is_done:
            # 뒤로 이동
            back_facing = (facing + 2) % 4
            bi = row + di[back_facing]
            bj = column + dj[back_facing]
            if 0 <= bi < N and 0 <= bj < M and room[bi][bj] != 1:
                row, column = bi, bj  # 뒤로 이동
            else:
                return  # 뒤가 벽이면 종료

        # 4. 청소 가능한 칸이 있는 경우
        else:
            if room[ni][nj] == 0:
                row, column, facing = ni, nj, next_facing  # 회전 후 전진


# 입력 처리
N, M = map(int, input().split())  # N * M 크기의 방
r, c, d = map(int, input().split())  # 로봇 위치 (r,c), 방향 d

room = [list(map(int, input().split())) for _ in range(N)]

di = [-1, 0, 1, 0]  # 북, 동, 남, 서
dj = [0, 1, 0, -1]
cnt_cleaned = 0

clean(r, c, d)
print(cnt_cleaned)

















