import sys
sys.stdin = open('input.txt')


def maze_run(y, x):
    global is_possible
    visiting_queue = [(y, x)]          # 받는 인자 2개 니까 튜플로 리스트 안에 저장
    while visiting_queue:                       # 큐에 대기 중인 값이 있으면 반복
        y, x = visiting_queue.pop(0)                 # 큐니까 제일 앞 부터 FIFO

        for k in range(4):                                       # 상 하 좌 우
            if 0 <= y + di[k] < 16 and 0 <= x + dj[k] < 16:    # 범위 안에 있고
                if maze[y][x] == '3':          # 도착하면 '가능함' 채크 후 return
                    is_possible = True
                    return

                if visited[y + di[k]][x + dj[k]]:        # 왔던 곳이면 continue
                    continue

                if maze[y + di[k]][x + dj[k]] == '1':        # 벽이면 continue
                    continue

                ni = y + di[k]                           # (y, x) 값 다음 값으로
                nj = x + dj[k]
                visited[ni][nj] = visited[y][x] + 1          # visited -> True
                visiting_queue.append((ni, nj))            # 다음값 큐에 더해주기


di = [-1, 0, 1, 0]                                          # 상 하 좌 우 delta
dj = [0, 1, 0, -1]

for _ in range(10):
    test_case = int(input())                                       # test_case
    maze = [list(input()) for _ in range(16)]                       # 미로 배열
    visited = [[0] * 16 for _ in range(16)]               # 방문 정보 저장할 배열
    is_possible = False

    for i in range(16):                             # 전체 순회해서 시작 지점 찾기
        for j in range(16):
            if maze[i][j] == '2':
                start_i = i
                start_j = j

    visited[start_i][start_j] = 1             # 시작점 방문 여부는 미리 True로 해줌
    maze_run(start_i, start_j)                                # 메이즈 러너 시작!

    if is_possible:                                                      # 가능
        print(f'#{test_case} 1')
    else:                                                              # 불가능
        print(f'#{test_case} 0')
