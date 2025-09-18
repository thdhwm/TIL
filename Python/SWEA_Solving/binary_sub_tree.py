import sys
sys.stdin = open('input.txt')


def sub_tree(node):
    global cnt
    if left_child[node] != 0:
        cnt += 1
        sub_tree(left_child[node])

    if right_child[node] != 0:
        cnt += 1
        sub_tree(right_child[node])


T = int(input())

for test_case in range(1, T + 1):
    E, N = map(int, input().split())
    pairs = list(map(int, input().split()))
    cnt = 1

    left_child = [0] * (E + 2)   # E + 1 nodes, 1 base idx therefore E + 2
    right_child = [0] * (E + 2)

    for i in range(len(pairs))[::2]:
        if left_child[pairs[i]] == 0:
            left_child[pairs[i]] = pairs[i + 1]

        else:
            right_child[pairs[i]] = pairs[i + 1]

    sub_tree(N)

    print(f'#{test_case} {cnt}')

