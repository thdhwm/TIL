# 1 2 3
# 4 5 6
# 7 8 0
# 으로 정렬하기위한 최소 이동 수

# ex.
# 1 0 3
# 4 2 5
# 7 8 6
# -> 3 번

# 3 6 0
# 8 1 2
# 7 4 5
# -> -1 (불가능)
# ##########################################################################
from collections import deque


def bfs():
    visited = {start}
    q = deque([(start, 0)])
    while q:
        now_str, cnt = q.popleft()  # 현재 문자열, 이동 횟수
        if now_str == "123456780":  # 타겟 문자열과 같으면 그 때의 이동 횟수 리턴
            return cnt

        idx = now_str.index("0")  # 0인 곳의 인덱스
        i, j = divmod(idx, 3)  # 이차원 맵 내 좌표로 변환
        for k in range(4):  # 4방향 중 위치 바꿀 수 있는 곳
            ni = i + di[k]
            nj = j + dj[k]
            if 0 > ni or 3 <= ni or 0 > nj or 3 <= nj:
                continue

            next_str = list(now_str)  # 위치 교환 쉽게 하기 위해 리스트로 변환
            next_idx = ni * 3 + nj  # 위치 교환할 인덱스
            next_str[idx], next_str[next_idx] = next_str[next_idx], next_str[idx]
            next_str = ''.join(next_str)  # 문자열로 재변환

            if next_str in visited:  # 이미 방문한 곳인지 확인
                continue

            visited.add(next_str)
            q.append((next_str, cnt + 1))

    return -1  # 불가능


start = ""
di = [-1, 0, 1, 0]
dj = [0, -1, 0, 1]
for _ in range(3):
    start += ''.join(list(input().split()))

print(bfs())



