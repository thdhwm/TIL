import sys
sys.stdin = open('input.txt')


def pick_me(arr_i):
    global min_sum

    for i in range(N):
        if sum(visited) == N:
            sum_numbers = sum(numbers)
            if min_sum > sum_numbers:
                min_sum = sum_numbers
            return

        if min_sum <= sum(numbers):
            return

        if visited[i] == 1:
            continue

        numbers.append(matrix[arr_i][i])
        visited[i] = 1
        pick_me(arr_i + 1)
        visited[i] = 0
        numbers.pop()


T = int(input())

for test_case in range(1, T + 1):
    N = int(input())
    matrix = [list(map(int, input().split())) for _ in range(N)]
    visited = [0] * N
    min_sum = 21e8
    numbers = []

    pick_me(0)
    print(f'#{test_case} {min_sum}')
