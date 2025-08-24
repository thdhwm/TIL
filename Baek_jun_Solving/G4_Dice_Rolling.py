from collections import deque
import sys
sys.stdin = open('input.txt')
# BOJ 14499


def east(dice, i, j):
    if M <= j + 1:
        return
    else:
        dice[3], dice[0], dice[2], dice[5] = dice[5], dice[3], dice[0], dice[2]
        if table[i][j + 1] == 0:
            table[i][j + 1] = dice[5]
            print(dice[0])
        else:
            dice[5] = table[i][j + 1]
            table[i][j + 1] = 0
            print(dice[0])
        return (i, j + 1)


def west(dice, i, j):
    if 0 > j - 1:
        return
    else:
        dice[3], dice[0], dice[2], dice[5] = dice[0], dice[2], dice[5], dice[3]
        if table[i][j - 1] == 0:
            table[i][j - 1] = dice[5]
            print(dice[0])
        else:
            dice[5] = table[i][j - 1]
            table[i][j - 1] = 0
            print(dice[0])
        return (i, j - 1)


def north(dice, i, j):
    if 0 > i - 1:
        return
    else:
        dice[1], dice[0], dice[4], dice[5] = dice[0], dice[4], dice[5], dice[1]
        if table[i - 1][j] == 0:
            table[i - 1][j] = dice[5]
            print(dice[0])
        else:
            dice[5] = table[i - 1][j]
            table[i - 1][j] = 0
            print(dice[0])
        return (i - 1, j)


def south(dice, i, j):
    if N <= i + 1:
        return 
    else:
        dice[1], dice[0], dice[4], dice[5] = dice[5], dice[1], dice[0], dice[4]
        if table[i + 1][j] == 0:
            table[i + 1][j] = dice[5]
            print(dice[0])
        else:
            dice[5] = table[i + 1][j]
            table[i + 1][j] = 0
            print(dice[0])
        return (i + 1, j)


def roll_dice(i, j):
    dice = [0, 0, 0, 0, 0, 0]   
    # 1, 6, 5, 2, 4, 3    초기 상태 윗면 1, 동쪽 3
    funcs = [east, west, north, south]

    while order_que:
        move = order_que.popleft()
        next = funcs[move - 1](dice, i, j)
        if next:
            i, j = next

    return


N, M, x, y, K = map(int, input().split()) # 세로, 가로, 주사위 좌표 x,y, 명령 수
table = [list(map(int, input().split())) for _ in range(N)]
order_que = deque(list(map(int, input().split())))

roll_dice(x, y)
# order: 1 -> 동쪽, 2 -> 서쪽, 3 -> 북쪽, 4 -> 남쪽




