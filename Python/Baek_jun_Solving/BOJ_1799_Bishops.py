import sys
sys.stdin = open('input.txt')

N = int(input())   # N * N
board = [list(map(int, input().split())) for _ in range(N)]



# for row in range(N):
#     print(board[row])