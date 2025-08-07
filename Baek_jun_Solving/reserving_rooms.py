N = int(input())    # 회의 수
table = [[0, 0] for _ in range(N)]    # time table
total = 0
fastest = 0

for i in range(N):
    table[i] = list(map(int, input().split()))          # table input done

for i in range(N - 1, 0, -1):        # bubble sort based on finishing time
    for j in range(i):
        if table[j][1] > table[j + 1][1]:
            table[j][1], table[j + 1][1] = table[j + 1][1], table[j][1]

fastest = table[0][1]
total += 1

for i in range(N):
    if table[i][0] < fastest:    # if it's past starting time, continue
        continue
    else:
        fastest = table[i][1]
        total += 1

print(total)

############ time out error - need more efficent sorting algorithm #################

