import sys
sys.stdin = open('input.txt')

T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    lines = []
    cnt_cross = 0

    for _ in range(N):
        a, b = map(int, input().split())
        lines.append((a, b))

    for i in range(N):
        start1, end1 = lines[i]
        for j in range(i + 1, N):
            start2, end2 = lines[j]

            if (start1 - start2) * (end1 - end2) < 0:
                cnt_cross += 1

    print(f'#{test_case} {cnt_cross}')