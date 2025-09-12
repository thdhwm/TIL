T = int(input())

for test_case in range(1, T + 1):
    N = int(input())
    students = [0] + list(map(int, input().split()))    # 1-based idx
    grouped = [1] * (N + 1)    # 그룹이 되었으면 -> 0으로   result = sum(grouped)


    # for i in range(1, len(students) + 1):
    #     root = i
    #     stack = []
    #
    #     while students[root] != i:
    #         root = students[root]
    #         stack.append(root)
    #
    #         if students[root] == root:
    #             grouped[root] = 0
    #             break
    #

# 리스트 쭉쭉 가다가,,, idx = value 인 노드 만나면 다시 역순으로..
# idx = value 인 노드를 못만나면 0