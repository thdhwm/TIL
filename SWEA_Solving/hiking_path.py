T = int(input())
dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

def hiking_down(i, j):

    start = table[i][j]
    lowest = table[i][j]

    for k in range(4):
        if 0 <= i + dy[k] < N and 0 <= j + dx[k] < N:
            if start > table[i + dy[k]][j + dx[k]] and lowest > table[i + dy[k]][j + dx[k]]:
                lowest = table[i + dy[k]][j + dx[k]]
                lowest_i = i + dy[k]
                lowest_j = j + dx[k]
    
    if lowest != table[i][j]:
        return 1 + hiking_down(lowest_i, lowest_j)
    
    return 1

for t in range(1, T + 1):
    N = int(input()) # matrix size
    table = [list(map(int, input().split())) for _ in range(N)]
    path_length = 1
    max_length = 0

    for i in range(N):
        for j in range(N):
            local_length = hiking_down(i, j)
            if max_length < local_length:
                max_length = local_length

    print(f'#{t} {max_length}')



