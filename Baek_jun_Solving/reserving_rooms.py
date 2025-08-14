N = int(input())    # 회의 수
table = [[0, 0] for _ in range(N)]    # time table
total = 0
fastest = 0

for i in range(N):
    table[i] = list(map(int, input().split()))   # table input done ex. [[1, 4], [3, 5], [0, 6], .... [12, 14]]

table.sort(key=lambda x: (x[1], x[0]))

fastest = table[0][1]     # 첫번째 끝나는 시간 젤 빠름
total += 1                # 1개 배정 했으니까 +1

for i in range(1, N):
    if table[i][0] < fastest:    # if it's past starting time, continue
        continue

    else:
        fastest = table[i][1]
        total += 1

print(total)

# 첫 회를 카운트 하고, 전체 범위 반복 돌아서 틀렸었음 #
