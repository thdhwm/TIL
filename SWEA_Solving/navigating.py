import sys
sys.stdin = open('input.txt')


def dfs(now_at):
    global is_possible

    if now_at == 99:
        is_possible = 1
        return

    if link_lists.get(now_at, 'no_way') != 'no_way':
        for go_to in link_lists.get(now_at):     # ex. 0: [1,2]
            if visited[go_to] == 1:
                continue

            visited[go_to] = 1
            dfs(go_to)
            visited[go_to] = 0

    else:               # 연결된 곳이 없으면 return
        return


for _ in range(10):
    t, length = map(int, input().split())    # t - testcase 번호, roads - 길의 총 개수
    roads = list(map(int, input().split()))
    link_lists = {}      # 딕셔너리로 연결 리스트 저장
    visited = [0] * 100
    is_possible = 0

    for road in range(length):
        if link_lists.get(roads[2 * road], 'empty') == 'empty':
            link_lists[roads[2 * road]] = [roads[2 * road + 1]]
        else:
            link_lists[roads[2 * road]] += [roads[2 * road + 1]]

    visited[0] = 1
    dfs(0)

    print(f'#{t} {is_possible}')
