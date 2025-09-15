import sys
sys.stdin = open('input.txt')


def find(x):
    if x == parent[x]:
        return x

    parent[x] = find(parent[x])
    return parent[x]


def union(a, b):
    parent_a = find(a)
    parent_b = find(b)

    if parent_a == parent_b:
        return

    if parent_a < parent_b:  # union, push all population to parent
        population[parent_a] += population[parent_b]
        population[parent_b] = 0
        parent[b] = parent_a

    else:
        population[parent_b] += population[parent_a]
        population[parent_a] = 0
        parent[a] = parent_b


def war(a, b):
    parent_a = find(a)
    parent_b = find(b)

    if population[parent_a] == population[parent_b]:
        union(0, parent_a)        # draw, both perish
        union(0, parent_b)

    elif population[parent_a] > population[parent_b]:
        union(0, parent_b)        # union loser to 0

    else:
        union(0, parent_a)


T = int(input())

for test_case in range(1, T + 1):
    N = int(input())                # num of countries
    population = [0] + list(map(int, input().split()))
    parent = [i for i in range(N + 1)]
    Q = int(input())      # num of funcs 1 <= Q <= 100
    cnt = 0
    for _ in range(Q):
        func, aCountry, bCountry = input().split()
        cA = ord(aCountry) - 64    # ord('A') = 65 ~ ord('Z') = 90
        cB = ord(bCountry) - 64

        if func == 'alliance':
            union(cA, cB)

        elif func == 'war':    # defeated country -> union(0, defeated)
            war(cA, cB)

    # circuit all nodes -> if parent != 0 -> cnt += 1
    for i in range(N + 1):
        if find(i) != 0:
            cnt += 1

    print(f'#{test_case} {cnt}')
