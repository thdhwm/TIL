import sys
sys.stdin = open('input.txt')


def swaaaap(arr, depth):
    global max_prize
    board = arr[:]
    prev = ''.join(arr)

    if depth == 0:
        max_prize = max(max_prize, int(prev))
        return

    if prev in memo:
        return

    memo.append(prev)
    for i in range(len(board)):
        for j in range(len(board)):
            if i >= j:
                continue

            board[i], board[j] = board[j], board[i]
            swaaaap(board, depth - 1)
            board[i], board[j] = board[j], board[i]


T = int(input())

for test_case in range(1, T + 1):
    scores, swaps = input().split()
    boards = list(scores)
    max_prize = 0
    memo = []

    swaaaap(boards, int(swaps))
    print(f'#{test_case} {max_prize}')

