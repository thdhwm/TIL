N, M = map(int, input().split())
board = [[0]*M for _ in range(N)]
count_w = 0
count_b = 0

for i in range(N):
    board[i] = list(input())

for i in range(N):
    for j in range(M):
        if board[i][j] == 'W':
            count_w += 1
        else:
            count_b += 1

# b가 많은거로 가정
if count_w > count_b:
    count_w, count_b = count_b, count_w

if count_w < 32:
    change_color = 32 - count_w
else:
    change_color = 0

print(change_color)
