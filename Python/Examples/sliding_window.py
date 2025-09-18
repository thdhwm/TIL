# 매 번 입력 붙여넣기가 힘드니, 파일에서 입력을 받아오는 방식
import sys
sys.stdin = open("input.txt")


# 슬라이딩 윈도우 기본 코드
T = int(input())

for tc in range(1, T + 1):
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))
    now = sum(arr[:M])
    min_value, max_value = now, now

    for i in range(N - M):
        # 옛날 건 빼주고, 다음 건 더해준다.
        # - 변화량만 계산
        # - 슬라이싱보다 빠르다.
        now = now - arr[i] + arr[i + M]
        min_value = min(min_value, now)
        max_value = max(max_value, now)

    print(f'#{tc} {max_value - min_value}')


    