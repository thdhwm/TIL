import sys
sys.stdin = open('input.txt')
# T = int(input())
#
#
# def locating(arr, time):
#     global ans
#     if not arr:        # 기다리는 사람 없음 다들어간거임
#         ans = time
#         return
#
#     start, end = arr[0]   # 그리디 회의실
#     waiting = []
#     for i in range(1, len(arr)):
#         now_start, now_end = arr[i]
#         if now_start <= end:
#             waiting.append(arr[i])
#         else:
#             start, end = arr[i]
#     next_from_to = waiting[:]     # 리스트 넘겨줄 때는 복사 조심
#     locating(next_from_to, time + 1)     # 재귀로 기다리는 사람들 처리
#
#
#
# for test_case in range(1, T + 1):
#     N = int(input())
#     from_to = []
#     ans = 0
#     for _ in range(N):
#         sRoom, eRoom = map(int, input().split())
#         if sRoom > eRoom:
#             sRoom, eRoom = eRoom, sRoom
#         from_to.append((sRoom, eRoom))  # input 다 받음
#
#     from_to.sort(key=lambda x: x[1])    # 회의실 문제처럼 풀거임
#
#     locating(from_to, 0)
#
#     print(f'#{test_case} {ans}')
# ###############################################################
T = int(input())

for test_case in range(1, T + 1):    # 겹치는 구간 수 만큼 시간이 걸린다
    N = int(input())
    hallway = [0] * 201

    for _ in range(N):
        sRoom, eRoom = map(int, input().split())
        if sRoom > eRoom:
            sRoom, eRoom = eRoom, sRoom

        sIdx = (sRoom - 1) // 2
        eIdx = (eRoom - 1) // 2

        for idx in range(sIdx, eIdx + 1):
            hallway[idx] += 1       # 구간수 기록

    result = max(hallway)     # 겹치는 구간 가장 많은 경우

    print(f'#{test_case} {result}')


