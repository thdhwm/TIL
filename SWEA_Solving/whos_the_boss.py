import sys
sys.stdin = open('input.txt')

T = int(input())

for test_case in range(1, T + 1):
    N = int(input())
    table = [list(map(int, input().split())) for _ in range(N)]
    boss = []
    under = []
    for i in range(N):
        if table[i][0] == 1:
            boss.append(i)

        if table[0][i] == 1:
            under.append(i)

    print(f'#{test_case} boss:{boss[0]} / under:', end='')
    for i in range(len(under)):
        print(under[i], end=' ')
    print('')
