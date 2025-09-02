import sys
sys.stdin = open('input.txt')
# union, find, rank
# 3 ≤ n ≤ 500,000,  3 ≤ m ≤ 1,000,000


def find(parent, a):    # find(a) == find(b) ==>> cycle!!!
    root = a
    while parent[root] != root:
        root = parent[root]

    while parent[a] != a:
        next_node = parent[a]
        parent[a] = root
        a = next_node

    return root


def union(parent, rank, a, b):
    global is_cycle
    root_a = find(parent, a)
    root_b = find(parent, b)

    if root_a == root_b:
        is_cycle = 1
        return

    if rank[root_a] < rank[root_b]:
        parent[root_a] = root_b
    elif rank[root_b] < rank[root_a]:
        parent[root_b] = root_a
    else:
        parent[root_b] = root_a
        rank[root_a] += 1

    return


n, m = map(int, input().split())
cnt_turns = 0
is_cycle = 0
parent = [i for i in range(n)]
rank = [0] * n

for _ in range(m):
    start, end = map(int, input().split())
    cnt_turns += 1
    union(parent, rank, start, end)
    if is_cycle:
        break

if is_cycle:
    print(cnt_turns)
else:
    print(0)
