from heapq import heappush, heappop, heapify
import sys
sys.stdin = open('input.txt')

T = int(input())

for test_case in range(1, T + 1):
    N = int(input())
    q = list(map(int, input().split()))
    heap = []
    last = N - 1
    ancestor = 0

    for i in range(len(q)):
        heappush(heap, q[i])

    while last != 0:
        ancestor += heap[(last - 1) // 2]
        last = (last - 1) // 2

    print(f'#{test_case} {ancestor}')
