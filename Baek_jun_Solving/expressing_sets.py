def find(parent, x):
    root = x
    while parent[root] != root: 
        root = parent[root]
    
    while x != root:
        parent[x], x = root, parent[x]
    return root

def union(parent, a, b):
    a = find(parent, a)
    b = find(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


n, m = map(int, input().split()) # num of sets 0 ~ n,   m -> number of funcs

# if input -> 0 a b  -> union
# if input -> 1 a b  -> same?

parent = [i for i in range(n + 1)]

for _ in range(m):
    func, a, b = map(int, input().split())
    if func == 0:
        union(parent, a, b)
    else:
        print('YES' if find(parent, a) == find(parent, b) else 'NO')



