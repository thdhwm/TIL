from heapq import heappush, heappop, heapify
import sys
sys.stdin = open('input.txt')


def calc(start):    # start = 1
    if not heap[start].isdecimal():
        if heap[start] == '+':
            return calc(2 * start) + calc(2 * start + 1)

        elif heap[start] == '-':
            return calc(2 * start) - calc(2 * start + 1)

        elif heap[start] == '*':
            return calc(2 * start) * calc(2 * start + 1)

        elif heap[start] == '/':
            return calc(2 * start) / calc(2 * start + 1)

    else:
        return int(heap[start])

    return


for test_case in range(1, 11):
    N = int(input())
    heap = [''] * (N + 1)

    for _ in range(N):
        info = list(input().split())
        if len(info) == 2:
            heap[int(info[0])] = info[1]

        else:
            heap[int(info[0])] = (info[1], info[2], info[3])


    print(calc(1))



    # print(f'#{test_case} {heap}')
