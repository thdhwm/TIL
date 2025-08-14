def recur(n):
    for i in range(n):
        if visited[i]:
            continue

        # 현재 i 번 째 열을 선택
        visited[i] = 1
        # 다음 재귀 호출 코드 (다음 행을 봐라)
        recur(n + 1)
        # 되돌아 왔을 때, 계산한 값을 초기화
        visited[i] = 0


for t in range(1, 11):
    N = int(input())
    visited = [0] * N

    recur(N)
    # print(f'#{t}')
