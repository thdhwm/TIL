N, M = map(int, input().split())
baskets = [0] * N

for q in range(1, N + 1):
    baskets[q - 1] = q

for _ in range(M):
    i, j = map(int, input().split())
    swap_baskets = baskets[i - 1: j]

    for k in range(len(swap_baskets) // 2):
        swap_baskets[k], swap_baskets[-1 - k] = swap_baskets[-1 - k], swap_baskets[k]

    baskets[i - 1: j] = swap_baskets

print(*baskets)






