import sys
sys.stdin = open('input.txt')
# BOJ 21608

N = int(input())
table = [[0] * N for _ in range(N)]
kindred = {}
di = [-1, 0, 1, 0]
dj = [0, 1, 0, -1]
# 좋아하는 학생 수, 인접 빈 칸 수

for _ in range(N * N):
    student, *friends = map(int, input().split())
    kindred[student] = friends

    for i in range(N):
        for j in range(N):
            max_vacancy = 0
            max_friend = 0
            vacancy = 0
            friend = 0
            for k in range(4):
                ni = i + di[k]
                nj = j + dj[k]

                if 0 <= ni < N and 0 <= nj < N:    # for kindred in range
                    if table[ni][nj] == 0:
                        vacancy += 1

                    if table[ni][nj] in friends:
                        friend += 1

                    
print(kindred)
