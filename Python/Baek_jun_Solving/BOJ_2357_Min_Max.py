import sys
sys.stdin = open('input.txt')

# min heap, max heap 만들면 되는거?
# 안되겠냉...

# 세그먼트 트리 구축
def build(node, start, end):
    if start == end:
        tree[node] = (arr[start], arr[start])
        return
    mid = (start + end) // 2
    build(2 * node, start, mid)
    build(2 * node + 1, mid + 1, end)

    # 자식 노드들의 값으로 부모 노드 값 갱신
    left_min, left_max = tree[2 * node]
    right_min, right_max = tree[2 * node + 1]
    tree[node] = (min(left_min, right_min), max(left_max, right_max))

# 특정 구간의 최솟값과 최댓값 찾기
def query(node, start, end, l, r):
    if r < start or end < l: # 범위 밖
        return (float('inf'), float('-inf'))
    if l <= start and end <= r: # 노드 범위가 쿼리 범위에 완전히 포함
        return tree[node]

    mid = (start + end) // 2
    left_query = query(2 * node, start, mid, l, r)
    right_query = query(2 * node + 1, mid + 1, end, l, r)

    # 두 쿼리 결과의 최솟값과 최댓값 결합
    return (min(left_query[0], right_query[0]), max(left_query[1], right_query[1]))

# 입력 받기
tree = []    # 세그먼트 트리의 노드를 저장할 배열 (min, max 쌍)
arr = []    # 각 노드에는 (최솟값, 최댓값) 튜플을 저장

N, M = map(int, input().split())
for _ in range(N):
    arr.append(int(input()))

# 세그먼트 트리 초기화 (트리 크기는 배열 크기의 4배)
tree = [(0, 0)] * (4 * N)
build(1, 0, N - 1)

# 쿼리 수행
for _ in range(M):
    a, b = map(int, input().split())
    # 인덱스 조정 (문제는 1-based, 배열은 0-based)
    result = query(1, 0, N - 1, a - 1, b - 1)
    print(result[0], result[1])


