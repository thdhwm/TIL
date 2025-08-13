N, M = map(int, input().split())
board = [list(input()) for _ in range(N)]
min_change = 64
for i in range(N - 7):    # 8 * 8 체스판으로 잘라야 하니까 인덱스는 -7 씩
    for j in range(M - 7):
        change_count = 0

# i + j 홀짝 으로 'W', 'B'
        for p in range(8):
            for q in range(8):
                if (i + j + p + q) % 2 == (i + j) % 2 and board[i + p][j + q] != board[i][j]:
                    change_count += 1

                elif (i + j + p + q) % 2 != (i + j) % 2 and board[i + p][j + q] == board[i][j]:
                    change_count += 1

        if change_count > 32:
            change_count = 64 - change_count

        if min_change > change_count:
            min_change = change_count

print(min_change)
