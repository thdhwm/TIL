N, K = map(int, input().split())    #  물품 수 N(1 ≤ N ≤ 100), max 무게 K(1 ≤ K ≤ 100,000)
knapsack = []

for _ in range(N):
    W, V = map(int, input().split())
    knapsack.append((W, V))

