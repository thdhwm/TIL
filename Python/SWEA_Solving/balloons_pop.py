# import time
import sys
sys.stdin = open('input.txt')


def find(arr, idx):
    left, right = 0, 0
    for k in range(1, N):
        if 0 > idx - k:
            break

        if arr[idx - k] == 0:
            continue

        left = idx - k
        break

    for k in range(1, N):
        if N < idx + k:
            break

        if arr[idx + k] == 0:
            continue

        right = idx + k
        break

    return left, right


def balloon(arr, total, cnt):
    global max_total

    now = arr[:]

    if sum(now) == 0:
        if max_total < total:
            max_total = total
        return

    for i in range(1, len(arr)):
        if now[i] == 0:
            continue

        left, right = find(now, i)
        if (left == 0 or right == 0) and cnt > 3:
            continue

        if left != 0 and right != 0:    # 주위 2개
            score = now[left] * now[right]

        elif left == 0 and right == 0:   # 마지막 1개
            score = now[i]

        else:                           # 주위 1개
            score = now[left + right]

        now[i] = 0
        balloon(now, total + score, cnt - 1)
        now[i] = balloons[i]

    return


T = int(input())

for test_case in range(1, T + 1):
    # start = time.time()
    N = int(input())
    balloons = [0] + list(map(int, input().split()))
    max_total = 0

    balloon(balloons, 0, N)
    # end = time.time()
    # print(f'#{test_case} {max_total} {end - start}')
    print(f'#{test_case} {max_total}')

# #########################################################################

# memoization 이용해서 풍선 쏜 상태, 그 때의 최대 점수 기록해놔서 풀면 더 빠르게 가능
