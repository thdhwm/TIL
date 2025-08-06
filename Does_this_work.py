N = int(input())
roads = list(map(int, input().split()))
cities = list(map(int, input().split()))
inv_cities = cities[::-1]

cheapest_index = 0
total = 0

while roads:
    cheapest = 21e8
    for i in range(1, len(inv_cities)):
        if inv_cities[i] <= cheapest:
            cheapest = inv_cities[i]
            cheapest_index = i
    total += cheapest * (sum(roads[-1: -(cheapest_index + 1): -1]))

    for _ in range(cheapest_index):
        roads.pop()
        cities.pop()

    inv_cities = cities[::-1]

print(total)
