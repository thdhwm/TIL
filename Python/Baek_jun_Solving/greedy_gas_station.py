N = int(input())    # N (2 ≤ N ≤ 100,000)
roads = list(map(int, input().split()))    # ex. [2, 3, 1]
cities = list(map(int, input().split()))    # ex. [5, 2, 4, 1]
cheapest = 21e8
total = 0

for i in range(len(roads)):
    if cheapest > cities[i]:
        cheapest = cities[i]

    total += (cheapest * roads[i])

print(total)
