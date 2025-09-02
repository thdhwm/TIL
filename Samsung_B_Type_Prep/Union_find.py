# 유니온 파인드(Union-Find)
# 유니온 파인드(또는 합집합-찾기, Disjoint-Set) 
# 집합을 관리하는 자료구조
# 노드들이 서로 다른 그룹(집합)에 속하는지 확인하거나 두 그룹을 합치는 데 사용 
# 주로 그래프에서 사이클 감지나 연결성 확인 문제에 활용
# Ex. Kruskal의 MST(최소 신장 트리), 연결 컴포넌트 문제 해결

# 3가지 연산으로 구성
# Find(찾기): 노드가 속한 집합의 대표(루트)를 찾음
# Union(합치기): 두 노드가 속한 집합을 하나로 합칩
# Same(동일 집합 확인): 두 노드가 같은 집합에 속하는지 확인 (선택적)
# B형 문제는 대규모 입력(N ≤ 10^6)을 다루므로 최적화가 필수

def find(parent, x):
    if parent[x] != x:     # if self is not parent
        parent[x] = find(parent, parent[x])    # compress path
    return parent[x]


def union(parent, a, b):
    a = find(parent, a)
    b = find(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


def same(parent, a, b):     # check if a, b has same parent
    return find(parent, a) == find(parent, b)


# init
n = 4     # number of nodes
parent = [i for i in range(n + 1)]      # parent list, N + 1 for idx based 

union(parent, 1, 2)
union(parent, 2, 3)
print(same(parent, 1, 3))
union(parent, 3, 4)
print(same(parent, 1, 4))
print(parent)

# #######################################################

# with massive amount of input find() func can
# reach depth deeper than pythons recursion limit
# so try making find() func with using while


def find_while(parent, a):
    root = a
    # find root node for a
    while parent[root] != root:    # root - temp to chg a
        root = parent[root]
    # compress path (flatten)
    while parent[a] != a:
        next_node = parent[a]
        parent[a] = root
        a = next_node

    return root


# to keep the tree flat as possible
# when conducting union() fuc
# unite the tree by rank
# rank represent height of the tree
# unite shorter tree under longer tree

# when initiating kruskal() func
# make list for rank
rank = [0] * (n + 1)


def union_by_rank(parent, rank, a, b):
    root_a = find(parent, a)
    root_b = find(parent, b)
    if root_a != root_b:
        if rank[root_a] < rank[root_b]:    # lower under higher
            parent[root_a] = root_b
        elif rank[root_a] > rank[root_b]:
            parent[root_b] = root_a
        else:    # same rank
            parent[root_b] = root_a
            rank[root_a] += 1







