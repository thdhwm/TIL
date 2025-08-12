N = int(input())
paper = [[-1] * 101 for _ in range(101)]
circum_paper = 0

for _ in range(N):
    x, y = map(int, input().split())
    for i in [y, y + 10]:
        for j in range(11):
            paper[i][x + j] = 0

    for j in [x, x + 10]:
        for i in range(11):
            paper[y + i][j] = 0

    for i in range(1, 10):
        for j in range(1, 10):
            paper[y + i][x + j] += 2

for i in range(101):
    circum_paper += paper[i].count(0)

print(circum_paper)

# 둘레 0 으로 해서 바꾸고 0 갯수 세기 했는디 안댐... 어림도 업음

