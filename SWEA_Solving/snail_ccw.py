N = int(input())
num_to_find = int(input())
table = [[0] * N for _ in range(N)]    # N*N 행렬 생성
numbers = N * N
layers = 0                                 # 1 껍질 씩

while N - (2 * layers) >= 1:
    # 아래 방향 N 칸
    for i in range(N - (2 * layers)):
        table[i + layers][0 + layers] = numbers
        numbers -= 1

    # 오른쪽 방향 N - 1 칸
    for i in range(N - 1 - (2 * layers)):
        table[N - 1 - layers][i + 1 + layers] = numbers
        numbers -= 1

        # 위 방향 N - 1 칸
    for i in range(N - 1 - (2 * layers)):
        table[N - 2 - i - layers][N - 1 - layers] = numbers
        numbers -= 1

        # 왼쪽 방향 N - 2 칸
    for i in range(N - 2 - (2 * layers)):
        table[0 + layers][N - 2 - i - layers] = numbers
        numbers -= 1

    layers += 1                   # 안으로 1 껍데기 들어감

for y in range(N):                           # 좌표 찾기 
    for x in range(N):
        if table[y][x] == num_to_find:
            found_y = y + 1
            found_x = x + 1


for i in range(N):
    print(' '.join(map(str, table[i])))

print(found_y, found_x)