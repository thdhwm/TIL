N = int(input())
N_list = list(map(int, input().split()))
M = int(input())
M_list = list(map(int, input().split()))

DAT_list = [0] * 20000001   # -10000000 ~ 10000000
                            # idx = 0 ~ 20000000, 0 = 10000000
result_list = [0] * M
for i in range(N):
    DAT_list[10000000 + N_list[i]] = 1

for i in range(M):
    if DAT_list[10000000 + M_list[i]] == 1:
        result_list[i] = 1

print(*result_list)
