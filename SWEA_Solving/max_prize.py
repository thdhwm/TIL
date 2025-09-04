import sys
sys.stdin = open('input.txt')

#
# def swap(arr, depth, prevs):
#     global max_prize
#
#     if depth == 0:
#         result = 0
#         for i in range(len(arr)):
#             result += arr[i] * (10 ** (len(arr) - i - 1))
#         if max_prize < result:
#             max_prize = result
#         return
#
#     board = arr[:]
#     prev_swap = prevs[:]
#     if len(arr) <= 4:
#         result = 0
#         for i in range(len(arr)):
#             result += arr[i] * (10 ** (len(arr) - i - 1))
#         if max_prize < result:
#             max_prize = result
#
#     for i in range(len(board)):
#         for j in range(len(board)):
#             if i >= j or (i, j) in prev_swap:
#                 continue
#             prev_swap.append((i, j))
#             board[i], board[j] = board[j], board[i]
#             swap(board, depth - 1, prev_swap)
#             board[i], board[j] = board[j], board[i]
#     return
#


def swaaaap(arr, depth):
    global max_prize
    prev = 0
    board = arr[:]
    num = int(''.join(board))

    if depth == 0:
        max_prize = max(max_prize, int(''.join(board)))
        return

    if prev == num:
        return

    for i in range(len(board)):
        for j in range(len(board)):
            if i >= j:
                continue

            board[i], board[j] = board[j], board[i]
            swaaaap(board, depth - 1)
            board[i], board[j] = board[j], board[i]
            prev = num


T = int(input())

for test_case in range(1, T + 1):
    scores, swaps = input().split()
    boards = list(scores)
    # max_prize = int(''.join(boards))
    max_prize = 0


    swaaaap(boards, int(swaps))
    print(f'#{test_case} {max_prize}')
    # if len(boards) == 1:
    #     print(f'#{test_case} {boards[0]}')
    #
    # else:
    #     swap(boards, swaps, prev)
    #     print(f'#{test_case} {max_prize}')
