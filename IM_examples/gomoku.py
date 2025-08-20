T = int(input())
dy = [-1, 0, 1, 1]     # 위 대각선, 가로, 대각선, 세로
dx = [1, 1, 1, 0]

for t in range(1, T + 1):
    board = [list(map(int,input().split())) for _ in range(19)]
    is_done = 0

    for i in range(19):                 # 태훈 (1) 이기는 경우
        for j in range(19):
            if board[i][j] == 1:
                for k in range(4):           # 각 방향마다 탐색
                    count_gomoku = 0
                    for m in range(5):
                        if 0 <= i + m * dy[k] < 19 and 0 <= j + m * dx[k] < 19:
                            if board[i + m * dy[k]][j + m * dx[k]] == 1:
                                count_gomoku += 1

                    if count_gomoku == 5:
                        if 0 <= i + (-1 * dy[k]) < 19 and 0 <= j + (-1 * dx[k]) < 19:   # 뒤에 1개 확인
                            if board[i + (-1 * dy[k])][j + (-1 * dx[k])] == 1:
                                count_gomoku += 1

                        if 0 <= i + (5 * dy[k]) < 19 and 0 <= j + (5 * dx[k]) < 19:     # 앞에 1개 확인
                            if board[i + (5 * dy[k])][j + (5 * dx[k])] == 1:
                                count_gomoku += 1

                    if count_gomoku == 5:                                   # 앞 뒤 확인 후 여전히 5 이면
                        print(f'#{t} Noheul WIN! ({i + 1}, {j + 1})')
                        is_done = 1
                        break
        if is_done:
            break
                                   
                
    for i in range(19):                 # 상대 (2) 이기는 경우
        for j in range(19):
            if board[i][j] == 2:
                for k in range(4):           # 각 방향마다 탐색
                    count_gomoku = 0
                    for m in range(5):
                        if 0 <= i + m * dy[k] < 19 and 0 <= j + m * dx[k] < 19:
                            if board[i + m * dy[k]][j + m * dx[k]] == 2:
                                count_gomoku += 1

                    if count_gomoku == 5:
                        if 0 <= i + (-1 * dy[k]) < 19 and 0 <= j + (-1 * dx[k]) < 19:   # 뒤에 1개 확인
                            if board[i + (-1 * dy[k])][j + (-1 * dx[k])] == 2:
                                count_gomoku += 1

                        if 0 <= i + (5 * dy[k]) < 19 and 0 <= j + (5 * dx[k]) < 19:     # 앞에 1개 확인
                            if board[i + (5 * dy[k])][j + (5 * dx[k])] == 2:
                                count_gomoku += 1

                    if count_gomoku == 5:                                   # 앞 뒤 확인 후 여전히 5 이면
                        print(f'#{t} Noheul LOSE T.T ({i + 1}, {j + 1})')
                        is_done = 1
                        break
        if is_done:
            break

    if is_done == 0:
        print(f'#{t} PLAYING')