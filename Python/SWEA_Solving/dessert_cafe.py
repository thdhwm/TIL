import sys
sys.stdin = open('input.txt')


def how_long(r, c):
    uRight = 0
    lRight = 0
    for n in range(1, N):   # upper right, lower right 대각선 길이 구하기
        dUpper = r - n
        dLower = r + n
        dBoth = c + n
        if 0 <= dUpper < N and 0 <= dBoth < N:
            uRight = n
        if 0 <= dLower < N and 0 <= dBoth < N:
            lRight = n
    return uRight, lRight


def cafe(si, sj, ul, ll):
    global max_dessert

    dessert_kind = []         #  카페 수 저장용 리스트
    uLength, lLength = ul, ll       #  대각선 길이
    if uLength < 1 or lLength < 1:     # 어느 한쪽으로도 1칸도 못간다면 return
        return

    if 2 * (uLength + lLength) <= max_dessert:   # max 값 보다 이미 작으면 return
        return

    now_i, now_j = si, sj
    for k in range(4):         # delta 시작
        if k % 2 == 0:         # 우상향, 좌하향
            for u in range(1, uLength + 1):
                ni = now_i + di[k]
                nj = now_j + dj[k]
                if 0 > ni or N <= ni or 0 > nj or N <= nj:   # 범위 밖으로 나가면 return
                    return

                if cafes[ni][nj] in dessert_kind:    # 같은 종류 들렀으면 불가능, return
                    return

                dessert_kind.append(cafes[ni][nj])
                now_i, now_j = ni, nj

        else:                  # 우하향, 좌상향
            for l in range(1, lLength + 1):
                ni = now_i + di[k]
                nj = now_j + dj[k]
                if 0 > ni or N <= ni or 0 > nj or N <= nj:  # 범위 밖으로 나가면 return
                    return

                if cafes[ni][nj] in dessert_kind:  # 같은 종류 들렀으면 불가능, return
                    return

                dessert_kind.append(cafes[ni][nj])
                now_i, now_j = ni, nj

    max_dessert = len(dessert_kind)      # return 없이 반복문 다 돌았으면 max 갱신


T = int(input())
di = [-1, 1, 1, -1]     # 우상, 우하, 좌하, 좌상 delta
dj = [1, 1, -1, -1]
for test_case in range(1, T + 1):
    N = int(input())
    cafes = [list(map(int, input().split())) for _ in range(N)]
    max_dessert = -1     # 없을 때 생각해서 -1로 초기화

    for i in range(N):      # 모든 점에 대해서
        for j in range(N):
            ul, ll = how_long(i, j)
            for p in range(ul):      #  모든 대각선 길이에 대해서
                for q in range(ll):
                    cafe(i, j, ul - p, ll - q)

    print(f'#{test_case} {max_dessert}')

    # 제일 큰 가능한 대각선 위 방향 d1 칸, 대각선 아래 방향 d2 칸 구해서 순회 후 카페 수
    # 중복이 있거나 해서 불가능 하면 -> d1, d2 를 각각 줄여가면서 max 카페 구하기
    # d1, d2 < 1 이면 불가능
    # max 값 -1 로 초기화 해서 불가능할 때 -1 출력하게