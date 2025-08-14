import sys
sys.stdin = open('input.txt')

from collections import deque

T = int(input())

for t in range(1, T + 1):
    N, M = map(int, input().split())
    # N = number of papers, M = idx of target paper you're looking for (starting with 0)
    priority = deque(list(map(int, input().split())))   # [1, 2, 3, 4]
    queue = deque([i for i in range(1, N + 1)])         # [1, 2, 3, 4]
    cnt_prints = 0
    target = queue[M]                                 # 3
    priority_max = max(priority)                      # 4
    printed = 0

    while target != printed:
        if priority[0] != priority_max:
            priority.append(priority.popleft())
            queue.append(queue.popleft())
        else:
            priority.popleft()
            printed = queue.popleft()
            if priority:
                priority_max = max(priority)
            cnt_prints += 1

    print(cnt_prints)
