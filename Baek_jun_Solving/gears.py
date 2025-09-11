from collections import deque
import sys
sys.stdin = open('input.txt', 'r')


def spin(row, direct):
    confirmed[row] = 1
    if 0 <= (row + 1) < 4 and confirmed[row + 1] == 0 and gears[row][2] != gears[row + 1][6]:
        spins[row + 1] = -direct
        spin(row + 1, -direct)

    if 0 <= (row - 1) < 4 and confirmed[row - 1] == 0 and gears[row][6] != gears[row - 1][2]:
        spins[row - 1] = -direct
        spin(row - 1, -direct)


gears = []
for _ in range(4):
    gears.append(deque(input()))   # 4 gears
    # each gear starting from north clock wise
    # N - 0, S - 1
    # same pole -> no rotation, diff pole -> other direction
K = int(input())    # number of rotations
for _ in range(K):
    gNo, direction = map(int, input().split())   # gNo - gear number 1~4
    # direction cw -> 1, ccw -> -1

    # [1, 0, 1, 0, 1, 1, 1, 1]   # right - 2 and left - 6
    # [0, 1, 1, 1, 1, 1, 0, 1]

    spins = [0] * 4          # spin_direction
    spins[gNo - 1] = direction

    confirmed = [0] * 4      # visited

    spin(gNo - 1, direction)    # 0 base idx
    for i in range(4):
        if spins[i] == 0:
            continue

        elif spins[i] == 1:    # cw
            gears[i].appendleft(gears[i].pop())

        elif spins[i] == -1:    # ccw
            gears[i].append(gears[i].popleft())

total = 0
for k in range(4):
    total += int(gears[k][0]) * (2**k)

print(total)