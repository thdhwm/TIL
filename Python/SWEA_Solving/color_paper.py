# N = int(input())
# paper = [[-1] * 101 for _ in range(101)]
# circum_paper = 0

# for _ in range(N):
#     x, y = map(int, input().split())
#     for i in [y, y + 10]:
#         for j in range(11):
#             paper[i][x + j] = 0

#     for j in [x, x + 10]:
#         for i in range(11):
#             paper[y + i][j] = 0

#     for i in range(1, 10):
#         for j in range(1, 10):
#             paper[y + i][x + j] += 2

# for i in range(101):
#     circum_paper += paper[i].count(0)

# print(circum_paper)

# # 둘레 0 으로 해서 바꾸고 0 갯수 세기 했는디 안댐... 어림도 업음

N = int(input())
paper = [[0] * 101 for _ in range(101)]
boarder_paper = 0
dy = [-1, 0, 1, 0]   # 델타 배열
dx = [0, 1, 0, -1]

for _ in range(N):           # 색종이 붙은 부분은 1 로
    y, x = map(int, input().split())
    for i in range(10):
        for j in range(10):
            paper[y + i][x + j] = 1

for p in range(101):
    for q in range(101):
        if paper[p][q] == 1:
            for k in range(4):
                ny, nx = p + dy[k], q + dx[k]  # 경계 밖이면 둘레 +1
                if ny < 0 or nx < 0 or ny >= 101 or nx >= 101:
                    boarder_paper += 1
                
                elif paper[ny][nx] == 0: # 주변이 비어 있으면 둘레 +1
                    boarder_paper += 1

print(boarder_paper)

