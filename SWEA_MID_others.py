T = int(input())
for tc in range(1, T+1):
    N = int(input())
    mat = [input().split() for _ in range(N)]
    m1 = [[mat[N-1-j][i] for j in range(N)] for i in range(N)]
    m2 = [[mat[N-1-i][N-1-j] for j in range(N)] for i in range(N)]
    m3 = [[mat[j][N-1-i] for j in range(N)] for i in range(N)]
    print(f"#{tc}")
    for i in range(N):
        print(''.join(m1[i]), ''.join(m2[i]), ''.join(m3[i]))