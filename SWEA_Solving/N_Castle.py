def recur(depth):
    global cnt_full

    for i in range(1, N + 1):
        if sum(visited) == N:
            cnt_full += 1
            return

        if visited[i]:
            continue

        # 현재 i 번 째 열을 선택
        visited[i] = 1
        # 다음 재귀 호출 코드 (다음 행을 봐라)
        recur(depth + 1)
        # 되돌아 왔을 때, 계산한 값을 초기화
        visited[i] = 0


for t in range(1, 11):
    N = int(input())
    visited = [0] * (N + 1)
    cnt_full = 0
    recur(0)
    print(f'#{t} {cnt_full}')
# ######## worked but was slow ##########
# ######## could be my computer issue ###